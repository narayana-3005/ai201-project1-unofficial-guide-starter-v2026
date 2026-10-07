# Run log — after_hybrid

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.55
- Runs per question: 3, caching off
- When: 2026-10-06 19:43

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| How are juniors and seniors ordered in the housing lottery? |   |   |   |
| How long is the wait at Kestrel Commons between 12:15 and 1:00? |   |   |   |
| How late in the semester can you declare a course pass/fail? |   |   |   |
| How much does it cost to wash a load of laundry in Aldridge Hall? |   |   |   |
| Do the CS 210 exams reuse the lab problems? |   |   |   |

> The Run columns are blank because `scorer.py` doesn't exist yet.
> Judge each question yourself by reading the output below, or build
> the scorer first and re-run.

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.55. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.869 | refused |
| How do I change the oil in a diesel engine? | 0.934 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.860 | refused |
| How do I write a for loop in Rust? | 0.900 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### How are juniors and seniors ordered in the housing lottery? — run 1

- Best distance: 0.2250 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, housing_morrow_house.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
Juniors and seniors are ordered by accumulated credit hours first, with ties broken randomly (source: admin_housing_lottery.txt).
```

### How are juniors and seniors ordered in the housing lottery? — run 2

- Best distance: 0.2250 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, housing_morrow_house.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
Juniors and seniors are ordered by accumulated credit hours first, with a random tie-break used only when necessary (source: admin_housing_lottery.txt).
```

### How are juniors and seniors ordered in the housing lottery? — run 3

- Best distance: 0.2250 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, advising_registration.txt, housing_morrow_house.txt, housing_old_brewhouse.txt, housing_tamsin_court.txt

```
Juniors and seniors are ordered by accumulated credit hours first, and only tie-break randomly in the housing lottery (source: admin_housing_lottery.txt).
```

### How long is the wait at Kestrel Commons between 12:15 and 1:00? — run 1

- Best distance: 0.2129 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt, transit_walking.txt

```
The wait at Kestrel Commons between 12:15 and 1:00 is 20 to 25 minutes. (source: dining_kestrel_commons.txt)
```

### How long is the wait at Kestrel Commons between 12:15 and 1:00? — run 2

- Best distance: 0.2129 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt, transit_walking.txt

```
The wait at Kestrel Commons between 12:15 and 1:00 is 20 to 25 minutes (source: dining_kestrel_commons.txt).
```

### How long is the wait at Kestrel Commons between 12:15 and 1:00? — run 3

- Best distance: 0.2129 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt, transit_walking.txt

```
The wait at Kestrel Commons between 12:15 and 1:00 is 20 to 25 minutes. (source: dining_kestrel_commons.txt)
```

### How late in the semester can you declare a course pass/fail? — run 1

- Best distance: 0.2072 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, course_biol_160.txt, course_math_220.txt

```
You can declare a course pass/fail as late as week eight, after you've seen your midterm. (source: admin_pass_fail_option.txt)
```

### How late in the semester can you declare a course pass/fail? — run 2

- Best distance: 0.2072 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, course_biol_160.txt, course_math_220.txt

```
You can declare a course pass/fail as late as week eight, after you've seen your midterm. (source: admin_pass_fail_option.txt)
```

### How late in the semester can you declare a course pass/fail? — run 3

- Best distance: 0.2072 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_pass_fail_option.txt, course_biol_160.txt, course_math_220.txt

```
You can declare a course pass/fail as late as week eight, after you've seen your midterm. (source: admin_pass_fail_option.txt)
```

### How much does it cost to wash a load of laundry in Aldridge Hall? — run 1

- Best distance: 0.1984 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt

```
It costs $1.75 to wash a load of laundry in Aldridge Hall (source: housing_aldridge_hall.txt).
```

### How much does it cost to wash a load of laundry in Aldridge Hall? — run 2

- Best distance: 0.1984 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt

```
It costs $1.75 to wash a load of laundry in Aldridge Hall (source: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt).
```

### How much does it cost to wash a load of laundry in Aldridge Hall? — run 3

- Best distance: 0.1984 (passed the gate)
- Sources retrieved: housing_aldridge_hall.txt, housing_aldridge_hall_laundry.txt, housing_innisfree_hall.txt, housing_innisfree_hall_laundry.txt, housing_old_brewhouse.txt

```
It costs $1.75 to wash a load of laundry in Aldridge Hall (source: housing_aldridge_hall.txt).
```

### Do the CS 210 exams reuse the lab problems? — run 1

- Best distance: 0.3599 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130.txt

```
Yes, the CS 210 exams reuse the lab problems (source: course_cs_210.txt).
```

### Do the CS 210 exams reuse the lab problems? — run 2

- Best distance: 0.3599 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130.txt

```
Yes, the CS 210 exams reuse the lab problems (source: course_cs_210.txt).
```

### Do the CS 210 exams reuse the lab problems? — run 3

- Best distance: 0.3599 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt, course_cs_340_exams.txt, course_engl_205_exams.txt, course_phys_130.txt

```
Yes, the exams in CS 210 reuse the lab problems (source: course_cs_210.txt).
```
