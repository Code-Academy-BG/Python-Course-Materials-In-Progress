import json
import os
import random

from oop_exercise.views import TEST_DATA_DIR

files = [
    "Orders_2021_09_15.json",
    "Orders_2021_09_16.json",
    "Orders_2021_09_26.json",
    "Orders_2021_10_16.json",
]

if __name__ == "__main__":
    for file in files:
        with open(os.path.join(TEST_DATA_DIR, file), "r") as source:
            loaded = json.load(source)

        for order in loaded:
            random.shuffle(order["details"])
        with open(os.path.join(TEST_DATA_DIR, file), "w") as output:
            json.dump(loaded, output)
