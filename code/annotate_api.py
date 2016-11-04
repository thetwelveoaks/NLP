import utilities
import re
import random

tree = utilities.parsexml("../dataset/APIs.xml")
root = tree.getroot()
rows = []
for row in root.findall("row"):
    rows.append(row)

# Randomly select 100 posts
random.seed(12345)
random.shuffle(rows)
for row in rows[100:]:
    root.remove(row)

tree.write("../dataset/API_Sample.xml", encoding = "utf-8")

rows = rows[:100]

# Auto annotate
count = 0
for row in rows:
    body = row.get("Body")
    pos = 0
    match_obj = utilities.api_pattern.search(body, pos)
    while pos < len(body) and (match_obj is not None):
        match_excep = utilities.excep_pattern.search(match_obj.string[match_obj.start(): match_obj.end()])
        if match_excep is None:
            prev = match_obj.string[:match_obj.start()]
            mid = "<api>" + match_obj.string[match_obj.start(): match_obj.end()] + "</api>"
            last = match_obj.string[match_obj.end():]
            body = prev + mid + last
            count += 1
        pos = match_obj.end();
        match_obj = utilities.api_pattern.search(body, pos)
    row.set("Body", body)

tree.write("../dataset/APIs_Auto_Annotated.xml", encoding = "utf-8")

print("Total APIs annotated: " + str(count))
