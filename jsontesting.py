import json
from collections import Counter
info_about_me = {"name": "Michele","has_a_dog": False}
datastore = {}
with open("info.json", "r") as f:
    datastore = json.load(f)
    bdaylist = datastore.values()
monthlist = []
for x in bdaylist:
    monthlist.append(x[0:2])
print(Counter(monthlist))
    
