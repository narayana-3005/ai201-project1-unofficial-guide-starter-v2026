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

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

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

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**

**Answer:**

```
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  |  |  |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**

**2.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
