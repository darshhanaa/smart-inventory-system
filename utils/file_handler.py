import json
import os


FILE_PATH = "data/inventory.json"


def load_data():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(products):
    with open(FILE_PATH, "w") as file:
        json.dump(products, file, indent=4)