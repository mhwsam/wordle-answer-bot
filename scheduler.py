# import yaml
# from scripts.wordle import run   # fine as-is, because scheduler.py is at repo root
# from scripts.render import render
# from pathlib import Path


# with open("config/games.yaml") as f:
#     config = yaml.safe_load(f)

# for game, details in config.items():
#     if game == "wordle":
#         winner, today, data = run(details["sources"])
#         if not winner:
#             print("[FAIL] No consensus")
#             continue
#         context = {"date": today, "answer": winner.upper()}
#         out_html = f"output/{details['output_prefix']}-{today}.html"
#         render(details["template"], context, out_html)
#         render(details["template"], context, "output/wordle-today.html")
#         print(f"[OK] Wordle {today} → {winner.upper()}")



import yaml
from scripts.wordle import run
from scripts.render import render
from pathlib import Path

with open("config/games.yaml") as f:
    config = yaml.safe_load(f)

for game, details in config.items():
    if game == "wordle":
        winner, today, data = run(details["sources"])
        answer = (winner or "UNKNOWN").upper()

        context = {"date": today, "answer": answer}

        # Daily archive page
        out_html = f"output/{details['output_prefix']}-{today}.html"
        render(details["template"], context, out_html)

        # Today permalink
        render(details["template"], context, f"output/{details['output_prefix']}-today.html")

        print(f"[OK] Wordle {today} → {answer}")
