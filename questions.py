"""
Your test questions.

Milestone 2 asks you to write five questions your system should be able to
answer from your corpus, specific enough to have a right answer.

`expects` is a word or short phrase a correct answer would contain, decided
before seeing any results. `OUT_OF_SCOPE` holds five questions the documents
clearly don't cover; criterion 3 needs five of them for "4 of 5".
"""

QUESTIONS = [
    # One sentence in admin_housing_lottery.txt holds the answer.
    {"question": "How are juniors and seniors ordered in the housing lottery?",
     "expects": "credit hours"},
    # Stated in both dining_kestrel_commons.txt and its _followup post.
    {"question": "How long is the wait at Kestrel Commons between 12:15 and 1:00?",
     "expects": "20 to 25"},
    # admin_pass_fail_option.txt has it; "week eight" also shows up in the
    # CS 340 posts about something else, so the phrase alone isn't enough.
    {"question": "How late in the semester can you declare a course pass/fail?",
     "expects": "week eight"},
    # Aldridge's price is in two posts (main + _laundry). Innisfree also
    # charges $1.75 a wash, so the building name has to do the work.
    {"question": "How much does it cost to wash a load of laundry in Aldridge Hall?",
     "expects": "$1.75"},
    # Nine "<course> — assessment" posts look alike; only the CS 210 ones
    # mention the labs being reused.
    {"question": "Do the CS 210 exams reuse the lab problems?",
     "expects": "lab problems"},
]

# Questions from a different world entirely. Your gate should refuse all five.
OUT_OF_SCOPE = [
    "What is the capital of Mongolia?",
    "How do I change the oil in a diesel engine?",
    "Who won the 1994 World Cup?",
    "What is the recommended dosage of ibuprofen for a headache?",
    "How do I write a for loop in Rust?",
]


def answered() -> list[dict]:
    """The questions you've actually filled in."""
    return [q for q in QUESTIONS if q.get("question", "").strip()]
