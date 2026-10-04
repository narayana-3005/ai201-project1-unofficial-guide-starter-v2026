# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
4 of 5 rather than 5 of 5 because two of my questions are deliberately
near-duplicates of other posts: Innisfree Hall charges the same $1.75 a wash as
Aldridge, and nine course "assessment" posts are written in the same shape as
the CS 210 one. I expect one of those to pull back the wrong post. Lower than 4
would mean retrieval is failing on questions whose answer sits in one plain
sentence, which in a corpus this small would be a real problem, not bad luck.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**
All five, because naming the file costs the model nothing: every excerpt in the
prompt is labelled `[from filename]` and the grounding instruction asks for it
by name. If even one answer leaves the source out, the instruction is not being
followed, and that is exactly the failure that makes an answer uncheckable.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

**Why this target:**
The five `OUT_OF_SCOPE` questions (Mongolia, diesel engines, the 1994 World
Cup, ibuprofen, Rust loops) share almost no vocabulary with posts about a
campus, so they should land far from every chunk. I'm allowing one miss rather
than demanding 5 of 5 because "dosage" and "headache" are close to the health
centre post and "for loop" could brush against the CS course posts. If more
than one gets through, the cutoff is too loose.

---

## 4. Chunks stand on their own

Every chunk in the index is between 100 and 600 characters, and all 5 chunks
printed by `python app.py chunks -n 5` start with the title line of the post
they came from and end on a complete sentence.

**Why this target:**
Posts in `campus_life` are 178 to 549 characters, each a title line plus one to
three short paragraphs. Under 100 characters a chunk is a lone paragraph like
"The bad: the elevator is out roughly one week per semester." which doesn't say
*which* building; over 600 it would be mixing two posts' worth of topics. The
title line is what tells you "Aldridge Hall" or "CS 210", so a chunk without it
can't answer anything on its own. All 5 rather than 4 of 5, because this is
deterministic code, not a model: if one chunk breaks the rule, the chunker has
a bug.

---

## 5. The cited source actually contains the answer

For at least 4 of my 5 test questions, the answer contains that question's
`expects` phrase from `questions.py`, and at least one file the answer names
really contains that phrase when I open it.

**Why this target:**
Criterion 2 only checks that a filename shows up. In this corpus that's easy to
pass while being wrong: there are seven `housing_*` buildings and nine courses
whose posts all look alike, so the model can cite `housing_innisfree_hall.txt`
for an Aldridge question and still "name a source". I care about the citation
being the right one, because that is what lets a student check the answer. 4
of 5 and not 5 of 5 for the same reason as criterion 1 — if retrieval brings
back the wrong building, the answer can't be right either.

---

<!-- UNIT 2: if a criterion turns out to be unmeasurable, add a revision
     UNDER it ("> Revised in unit 2: ..." plus why). Never edit or delete the
     original, and never lower a target just because you missed it. -->
