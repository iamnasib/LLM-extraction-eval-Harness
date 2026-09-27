import json

problems = 0

for line in open("data/cases.jsonl", "r", encoding="utf-8"):
    case = json.loads(line)

    for field in ("strengths","concerns"):
        for item in case["expected"][field]:
            if item not in case["summary_text"]:
                problems+=1
                print(f"{case["id"]} [{field}] not found verbatim: {item!r}")

print(problems)