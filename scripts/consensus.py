import re
from collections import defaultdict

VALID_WORD = re.compile(r"^[a-z]{5}$")

def normalize(word):
    if not word:
        return None
    w = word.strip().lower()
    m = re.search(r"[a-z]{5}", w)
    return m.group(0) if m else None

# def weighted_consensus(candidates, threshold=2.0):
def weighted_consensus(candidates, threshold=1.0):

    tally = defaultdict(float)
    explain = defaultdict(list)
    for c in candidates:
        v = normalize(c.get("value"))
        if not v or not VALID_WORD.match(v):
            continue
        w = float(c.get("weight", 1.0))
        tally[v] += w
        explain[v].append({"source": c["name"], "w": w})
    if not tally:
        return None, {}
    winner, score = max(tally.items(), key=lambda kv: kv[1])
    return (winner if score >= threshold else None), {
        "scores": dict(tally), "explain": dict(explain)
    }
