import json

from jsonschema import Draft202012Validator

schema = json.load(open("schemas/extraction.json", encoding="utf-8"))

validator = Draft202012Validator(schema)

failures = 0

for line in open("data/test.jsonl",encoding="utf-8"):
    case=json.loads(line)
    for error in validator.iter_errors(case["expected"]):
        failures+=1
        print(f"{case["id"]}: {error.message}")

print(failures)