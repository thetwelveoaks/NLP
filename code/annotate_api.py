import utilities
import re
import random


tree = utilities.parsexml("../Data_set/APIs.xml")
root = tree.getroot()
rows = []
for row in root.findall("row"):
    rows.append(row)

random.seed(12345)
random.shuffle(rows)
for row in rows[100:]:
    root.remove(row)

rows = rows[:100]

count = 0
for row in rows:
    body = row.get("Body")
    pos = 0
    match_obj = utilities.api_pattern.search(body, pos)
    while pos < len(body) and (match_obj is not None):
        prev = match_obj.string[:match_obj.start()]
        mid = "<api>" + match_obj.string[match_obj.start(): match_obj.end()] + "</api>"
        last = match_obj.string[match_obj.end():]
        body = prev + mid + last
        count += 1
        pos = match_obj.end();
        match_obj = utilities.api_pattern.search(body, pos)

    row.set("Body", body)
##    print(body)
##    newbody = input("Press Enter to continue...\n")
##    if newbody != "":
##        row.set("Body", newbody)
##    else:
##        row.set("Body", body)
##    f_body.write(body)


##for row in root.findall("row"):
##    print(row.get("Body"))
##    newbody = input("Press Enter to continue...")
##    if newbody != "":
##        row.set("Body", newbody)
        
tree.write("../Data_set/APIs_Annotated.xml")

print(count)
