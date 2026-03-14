import json

def save_to_json(data):

    with open("repos.json", "w") as file:
        json.dump(data, file, indent=4)

import csv

def save_to_csv(data):

    with open("repos.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["name", "stars", "language"])

        for repo in data:
            writer.writerow([repo["name"], repo["stars"], repo["language"]])        