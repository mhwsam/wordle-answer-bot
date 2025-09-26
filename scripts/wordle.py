import json, re
from datetime import date, datetime
from pathlib import Path
from fetch import get
from consensus import weighted_consensus

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output"
DATA = ROOT / "data"
OUT.mkdir(exist_ok=True, parents=True)
DATA.mkdir(exist_ok=True, parents=True)

def extract(html, patterns):
    for patt in patterns:
        m = re.search(patt, html, flags=re.IGNORECASE)
        if m: return m.group(1)
    return None

def run(sources):
    raw = []
    for s in sources:
        try:
            html = get(s["url"])
            value = extract(html, s["patterns"]) if s["type"] == "regex_list" else None
        except Exception:
            value = None
        raw.append({"name": s["name"], "value": value, "weight": s.get("weight",1.0)})
    winner, info = weighted_consensus(raw, threshold=2.0)

    today = date.today().isoformat()
    stamp = datetime.utcnow().isoformat() + "Z"

    # JSON truth
    data = {
        "game":"wordle","date":today,"answer":winner,
        "candidates":raw,"consensus":info,"generated_at":stamp
    }
    (DATA/f"wordle-{today}.json").write_text(json.dumps(data,indent=2),"utf-8")
    return winner, today, data
