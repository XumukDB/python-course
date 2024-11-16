import json


FILENAME = "input.json"
ROUND_CONSTANT = 3


def task() -> float:
    with open(FILENAME, 'r') as file:
        json_data = json.load(file)

    return round(sum([item["score"] * item["weight"] for item in json_data]), ROUND_CONSTANT)


print(task())
