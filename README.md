# The Unofficial Guide

**Narayana — corpus: `campus_life`** (88 short student posts about dining, housing, courses, transit and campus admin rules).

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

It answers questions about student life at one (fictional) university from `campus_life`, a set of 88 short posts students wrote for each other. The posts cover the residence halls (laundry prices, noise, what each building is like), the dining halls (wait times, hours, what's worth eating), nine courses (exams, workload, advice), and admin rules nobody explains properly (housing lottery, add/drop, pass/fail, parking, printing). Ask it something like "how late can I declare pass/fail?" or "when is Kestrel Commons busy?" and it finds the closest posts, answers only from them, and names the file it used. If nothing in the posts is close enough, it says "I don't have enough information about that" instead of guessing.

## Chunking Strategy

**Chunk size:** up to 300 characters of body text per chunk (`MAX_CHUNK_CHARS`), plus the post's title line. Bodies under 150 characters (`MIN_CHUNK_CHARS`) are folded into the chunk before them. In practice the chunks run 177 to 461 characters including the title, 304 on average, 92 chunks from 88 posts.

**Overlap:** no character overlap. Instead, **the post's title line is repeated at the top of every chunk** it produces.

**Function:** `chunker.py::split_documents`. The starter's `fallback_split` is still there, unchanged.

**What I saw in the documents:** every `campus_life` post has the same shape: a short title line ("Aldridge Hall — what it's actually like", "CS 210 Data Structures — assessment"), a blank line, and then one to three short paragraphs. Posts are 178 to 549 characters. Two things followed from that:

- **The starter's 800-character window never cut anything** (88 documents became 88 chunks). That isn't wrong for most posts, because a lot of them really are one thought. But the longer posts cover two different things, e.g. `health_center.txt` has walk-in hours *and* counselling, and `housing_innisfree_hall.txt` has the building/rooms *and* laundry/noise.
- **The only place a building or course is named is the title line.** Split a housing post on its paragraphs and you get "The bad: no air conditioning..." with no way of telling which hall. Repeating the title fixes that; character overlap wouldn't.

**Why 300:** I tried 250, 300, 400 and 500. At 500 only one post split; at 400 only two. At 300 the posts that split were the ones with two different topics (health centre, shuttle, the long housing posts). At 250 it started cutting single-thought posts like `admin_housing_lottery.txt` mid-explanation.

**Where I changed my mind:** I started with a minimum of 120 characters. One chunk came out as just "Re: The Atrium / Also worth saying: picked clean by 1:15 and not restocked again until the next morning." Picked clean... *what?* The `*_followup.txt` dining posts all end with a short paragraph like that. I raised the minimum to 150, which folds those tails back into their post (99 chunks became 92).

## Sample Chunks

Printed with `python app.py chunks --indices 6,54,59,69,70`, picked so that split posts appear and not only whole ones.

**Chunk 1** (one long paragraph kept whole): source: `admin_housing_lottery.txt#0`, produced by: `chunker.py::split_documents`

    On the housing lottery

    The housing lottery is not random in the way most people assume. Rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly. That means a senior who took summer courses reliably beats a senior who didn't. Numbers come out the second week of March and selection runs over four evenings.

**Chunk 2** (a whole post kept as one chunk): source: `dining_the_ridgeway_cafe.txt#0`, produced by: `chunker.py::split_documents`

    The Ridgeway Café

    Second-year here. Wait times: 10 to 15 minutes at 12:30, none after 2:00. The thing worth going for is the only place on campus with real espresso. The thing to know is that seating is tight; about 40 seats for a building of 900.

    Hours are 7:00am to 4:00pm weekdays only. Costs declining balance only, no meal swipes.

**Chunk 3** (second half of a post that split on a topic change): source: `health_center.txt#1`, produced by: `chunker.py::split_documents`

    The health centre

    Counselling is separate, in the same building, and has its own intake process with a shorter wait than people expect — usually three or four days for a first session.

**Chunk 4** (first half of a split housing post): source: `housing_innisfree_hall.txt#0`, produced by: `chunker.py::split_documents`

    Innisfree Hall — what it's actually like

    Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

    The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

**Chunk 5** (second half of the same post): source: `housing_innisfree_hall.txt#1`, produced by: `chunker.py::split_documents`

    Innisfree Hall — what it's actually like

    The bad: no air conditioning, which matters for the first three weeks of September.

    Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

## Sample Answer

**Question:** How are juniors and seniors ordered in the housing lottery?

**Answer** (full output of `python app.py ask "How are juniors and seniors ordered in the housing lottery?"`):

    (best distance 0.225, cutoff 0.55)

    Juniors and seniors are ordered by accumulated credit hours first, with any ties broken randomly. (source: admin_housing_lottery.txt)

    Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt, advising_registration.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

    1 model calls this session, 676 tokens (646 in, 30 out)

An off-topic question, for comparison (`python app.py ask "Who won the 1994 World Cup?"`). The gate refuses it before the model is called:

    (best distance 0.886, cutoff 0.55)

    I don't have enough information about that.

    0 model calls this session

**My relevance cutoff:** `THRESHOLD = 0.55` in `config.py` (the starter shipped 0.6).

Best distances from `python app.py retrieve "..."` against my chunker's index (92 chunks), top-k 5:

| Question | In corpus? | Best distance | Best chunk |
|---|---|---|---|
| How are juniors and seniors ordered in the housing lottery? | yes | 0.2250 | `admin_housing_lottery.txt#0` |
| How long is the wait at Kestrel Commons between 12:15 and 1:00? | yes | 0.2129 | `dining_kestrel_commons_followup.txt#0` |
| How late in the semester can you declare a course pass/fail? | yes | 0.2072 | `admin_pass_fail_option.txt#0` |
| How much does it cost to wash a load of laundry in Aldridge Hall? | yes | 0.1984 | `housing_aldridge_hall_laundry.txt#0` |
| Do the CS 210 exams reuse the lab problems? | yes | 0.3599 | `course_cs_210_exams.txt#0` |
| What is the capital of Mongolia? | no | 0.8246 | `course_hist_118_exams.txt#0` |
| How do I change the oil in a diesel engine? | no | 0.9340 | `admin_meal_plan_changes.txt#0` |
| Who won the 1994 World Cup? | no | 0.8859 | `course_hist_118_exams.txt#0` |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.8442 | `money_textbooks.txt#0` |
| How do I write a for loop in Rust? | no | 0.8960 | `course_hist_118_exams.txt#0` |

**The two groups:** in-corpus 0.198 to 0.360, out-of-corpus 0.824 to 0.934. Anything between about 0.4 and 0.8 separates these ten. That's too easy, because those off-topic questions come from a different world. So I tried ten more questions to see where the edges really are:

| Question | Covered? | Best distance | Best chunk |
|---|---|---|---|
| is the housing lottery random? | yes | 0.2541 | `admin_housing_lottery.txt#0` |
| when do parking permits sell out? | yes | 0.3074 | `admin_parking_permits.txt#0` |
| is there a campus bookstore discount for laptops? | partly (textbooks only) | 0.3862 | `money_textbooks.txt#0` |
| is the health centre good for urgent stuff? | yes | 0.4116 | `health_center.txt#0` |
| where should I sit in the library? | yes | 0.4775 | `study_library_hours.txt#0` |
| which dorm has air conditioning problems? | yes (Innisfree) | 0.5341 | `housing_aldridge_hall.txt#0` (wrong hall) |
| what time does the football stadium open? | no | 0.5655 | `dining_halden_hall_followup.txt#0` |
| how much is tuition per year? | no | 0.5727 | `admin_printing_quota.txt#0` |
| does the campus gym have a swimming pool? | no | 0.6518 | `housing_tamsin_court.txt#0` |
| who is the university president? | no | 0.7802 | `admin_wifi_and_accounts.txt#0` |

Campus-sounding questions the posts don't answer land at 0.57 to 0.78. Vaguer questions the posts *do* answer go up to 0.53. **0.55 sits between 0.534 and 0.566.** At the starter's 0.6, the tuition and stadium questions would get through the gate, and only the prompt would stand between them and a made-up answer.

**What 0.55 gets wrong:** there's only about 0.015 of margin on each side. A slightly vaguer phrasing of a real question will be refused, and a slightly closer uncovered question will get through. The laptop question (0.386) passes easily even though the posts only cover textbooks. The gate can't catch that kind of near miss, so the grounding instruction has to.

**Grounding instruction:** I tightened `GROUNDING_INSTRUCTION` in `generate.py`. The refusal wording is now exact. There's a new rule for look-alike posts: use only the document about the hall, course or place the question names, and never carry a fact over from a similar one. Seven halls share the same "Laundry costs $X wash, $Y dry" sentence, so that's the likeliest way to get an answer that is wrong but still cites a real file.

## How I Used AI

I used Claude Code (in a cloud session) throughout this unit.

**1. The chunker's minimum size.** I asked Claude to write a chunker that fits `campus_life`. Its first version split posts on blank lines, repeated the title on every chunk, and folded anything under 120 characters into its neighbour. Reading the printed chunks, one was just "Re: The Atrium / Also worth saying: picked clean by 1:15 and not restocked again until the next morning". You can't tell *what* gets picked clean. Every `*_followup.txt` dining post ends with a tail like that, so the minimum went up to 150. That merged those tails back in (99 chunks became 92) and kept the splits I wanted (health centre, shuttle, long housing posts).

**2. Wrong numbers, and a wrong chunk.** Claude's first Milestone 4 distances were all around 0.85 to 0.97, with nonsense matches (laundry posts for "capital of Mongolia"). The cause was that running `tools/smoke_test.py` had re-indexed the corpus with its fake embedder, and re-running `python app.py index` fixed it. Separately, when I edited the README on GitHub myself, I pasted a chunk from the wrong corpus (`thread_bike_commute.txt` from `advice_threads`, made by `fallback_split`). That's not what my system produces, so I replaced it with the five chunks `python app.py chunks --indices 6,54,59,69,70` prints for `campus_life`.

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

File: `results/run_2026-10-06_1926_before.md`, produced by `run_eval.py::main` (gate part by `run_eval.py::check_out_of_scope`). There is no `scorer.py`, so criteria 1, 2 and 5 were scored with `tools/score_runs.py` (run as `PYTHONPATH=. python tools/score_runs.py <results file>`). Criterion 1 is scored at file level: a question passes if a retrieved file contains its `expects` phrase. Most posts are a single chunk, so this is close to chunk level. Criteria 3 and 4 are deterministic, so one number goes in all three columns.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks stand on their own | all 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Real output (criterion 1, `store.py::search`, laundry question, run 1):

    Sources retrieved: housing_aldridge_hall_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt, housing_old_brewhouse_laundry.txt

Real output (criterion 2, `generate.py::answer_from_chunks`, laundry question, run 1):

    It costs $1.75 to wash a load of laundry in Aldridge Hall (source: housing_aldridge_hall_laundry.txt).

Real output (criterion 3, `run_eval.py::check_out_of_scope`, cutoff 0.55):

    refused  (best distance 0.825)  What is the capital of Mongolia?
    refused  (best distance 0.934)  How do I change the oil in a diesel engine?
    refused  (best distance 0.886)  Who won the 1994 World Cup?
    refused  (best distance 0.844)  What is the recommended dosage of ibuprofen for a headache?
    refused  (best distance 0.896)  How do I write a for loop in Rust?
    -> gate refused 5 of 5

Real output (criterion 4, `chunker.py::split_documents`, from `python app.py chunks -n 92`): shortest chunk 179 characters, longest 465, none outside 100 to 600. Sample chunk 1:

    On the add/drop deadline

    You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

Real output (criterion 5, CS 210 question, run 1) and the line in `course_cs_210_exams.txt` that backs it:

    Yes, the exams reuse the lab problems (source: course_cs_210.txt, course_cs_210_exams.txt).
    Do the labs even though they're only 10% — the exams reuse the lab problems.

## Verdicts

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | 5/5 in all three runs against a target of 4 of 5. Retrieval is deterministic, so the runs could not differ. |
| 2 | Every answer names a source | MET | All 15 answers ended with a `(source: ...)` line. Target was 5 of 5. |
| 3 | Gate stops out-of-corpus questions | MET | Refused 5 of 5, best distances 0.825 to 0.934 against a 0.55 cutoff. |
| 4 | Chunks stand on their own | MET | All 92 chunks are 179 to 465 characters. The 5 printed samples all start with the post title. I judged "ends on a complete sentence" by eye on those 5 only. |
| 5 | Cited source contains the answer | MET | In all 15 answers the phrase is in the answer and in at least one cited file. For CS 210, runs 2 and 3 cited only `course_cs_210.txt`, which also contains "lab problems", so they pass. |

Every criterion was met on the first try, so my targets were probably set safe. Criteria 1, 3 and 5 scored 5/5 every time and should have been 5 of 5.

## Diagnoses

I missed no criterion, so there is no failure to diagnose. The one pattern I saw was in retrieval, not in the criteria: on every question 3 to 4 of the top 5 chunks were off-target (the wrong hall, the wrong course, or an unrelated post), 18 of 25 slots in total. This is a retrieval-stage problem, because the semantic search blurs building names and course codes. It never reached the answers, because the grounding prompt kept the model on the right post.

## The Improvement

**What I changed:** I added BM25 keyword search to `store.py::search` and merged it with the semantic ranking by reciprocal rank fusion (k = 60). Each result keeps its semantic distance, so the gate in `gate.py` still reads meaning alone. `store.py` is the only file that changed (`git diff --stat 6c1ff54 HEAD` on `store.py config.py gate.py generate.py chunker.py` lists only `store.py`).

**Why I picked it:** my weak spots were wrong-building and wrong-course posts crowding the top 5 (for example Innisfree and Old Brewhouse for an Aldridge question). Building names and course codes are exact terms that semantic search glides past.

**A mistake I made and kept in the history:** my first "after" run (commit `80efc14`, `results/run_2026-10-06_1941_after.md`) was made before `store.py` had actually been changed. Its distances match the before run exactly, which shows retrieval is deterministic, but it is not a measurement of the improvement. The real after run is `results/run_2026-10-06_1943_after_hybrid.md`, from commit `0f2f0d1`.

### Run Log — After

File: `results/run_2026-10-06_1943_after_hybrid.md`, scored the same way as the before log.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks stand on their own | all 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Cited source contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |

Top-5 retrieval, before to after (relevant posts / off-target posts):

| Question | Before | After |
|---|---|---|
| Housing lottery | 1 / 4 | 1 / 4 |
| Kestrel wait | 2 / 3 | 2 / 3 |
| Pass/fail | 1 / 4 | 1 / 4 (the CS 340 post that shares "week eight" dropped out) |
| Aldridge laundry | 1 / 4 | 2 / 3 (`housing_aldridge_hall.txt` entered, Old Brewhouse laundry with the wrong price left) |
| CS 210 exams | 2 / 3 | 2 / 3 (BIOL 160 swapped for PHYS 130) |

Off-target slots went from 18 of 25 to 17 of 25. The gate still refused 5 of 5. The out-of-scope best distances moved slightly (Mongolia 0.825 to 0.869, ibuprofen 0.844 to 0.860, Rust 0.896 to 0.900) because fusion changes which chunks reach the top 5. That is harmless here, with a large margin to the 0.55 cutoff.

**Did it help?** Barely. The pass counts did not change, because they were already at the ceiling. The one real gain is on the Aldridge laundry question: one more on-topic post and one fewer off-target post in the top 5. The other four questions are unchanged in quality. The after laundry answers cite `housing_aldridge_hall.txt`, which contains "$1.75", so criterion 5 still passes.

## What's Still Broken

Every question still pulls 3 to 4 off-target chunks into the top 5, and hybrid search removed only one of them. I would next try a smaller top-k (3) or a rule that drops chunks far behind the best one. I stopped because all five criteria were met, so this noise never showed up in the pass counts and I had no failing test to aim at. The relevance gate also has only about 0.015 of margin on each side in my Unit 1 edge-case questions (0.534 vs 0.566), which this unit did not test.

## What I'd Do Differently

I would write criteria 1, 3 and 5 as 5 of 5, since they scored 5/5 in every run. I would rewrite criterion 1 to count how many of the top 5 chunks are on-topic, because "a retrieved chunk contains the answer" could not show the difference hybrid search made. I would check criterion 4's "ends on a complete sentence" in code on all 92 chunks, not by eye on 5. I would also build `scorer.py` before running the test, so I do not score by hand.

## How I Used AI (Unit 2)

I used Claude in chat to plan the unit, write `tools/score_runs.py`, and write the hybrid BM25 + reciprocal-rank-fusion version of `store.py::search`. It also caught that my first "after" run and its commit were made before `store.py` had changed (the distances were identical to the before run, and the commit listed no code file), so I re-applied the change and re-ran. The verdicts, diagnoses and the call on whether the change helped come from my own runs.
