import re, sys
from questions import QUESTIONS
D = "corpora/campus_life/documents/"
exp = {q["question"]: q["expects"].lower() for q in QUESTIONS}
def has(fn, ph):
    try:
        return ph in open(D + fn).read().lower()
    except FileNotFoundError:
        return False
txt = open(sys.argv[1]).read().split("## Real output", 1)[1]
tally = {1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0]}
for b in re.split(r"\n### ", "\n" + txt)[1:]:
    head, rest = b.split("\n", 1)
    q, run = head.rsplit(" — run ", 1)
    run = int(run.strip())
    srcs = re.search(r"Sources retrieved: (.*)", rest).group(1).split(", ")
    ans = rest.split("```")[1]
    cited = re.findall(r"\w+\.txt", ans)
    ph = exp[q]
    c1 = any(has(s, ph) for s in srcs)
    c2 = bool(cited)
    c5 = ph in ans.lower() and any(has(c, ph) for c in cited)
    for k, ok in enumerate((c1, c2, c5)):
        tally[run][k] += ok
        if not ok:
            print("FAIL c%d run %d: %s" % ((1, 2, 5)[k], run, q))
for r in (1, 2, 3):
    print("run %d: crit1 %d/5  crit2 %d/5  crit5 %d/5" % (r, *tally[r]))
