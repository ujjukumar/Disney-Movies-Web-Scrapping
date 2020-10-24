import json
import csv

all_data = []
file = "Disney_movies_data_final.csv"
with open(file, encoding="utf-8") as f:
	reader = csv.DictReader(f)
	for row in reader:
		all_data.append(dict(row))

with open("Disney_movies_data.json", "w", encoding="utf-8") as f:
	json.dump(all_data, f, indent=4)