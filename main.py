from scrappers import runners
import json

with open("./credentials.json", "r") as f:
    credentials = json.load(f)

for provider in credentials.keys():
    titles = runners[provider](**credentials[provider])
    print(titles)
