from scrappers import runners
import json

with open("./credentials.json", "r") as f:
    credentials = json.load(f)

my_list = []
for provider in credentials.keys():
    titles = runners[provider](**credentials[provider])
    my_list.extend(titles)

print(my_list)
