import re
from utilities import parsexml, regex

recogniser = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\([_a-zA-z0-9\.+\-*/%]*(,[_a-zA-z0-9\.+\-*/%]*)*\)")
api_tag = re.compile("<api>" + ".+?" + "</api>")

api_tree = parsexml("../dataset/APIs_Fully_Annotated.xml")
api_root = api_tree.getroot()
api_set = set()
count = 0

allmatches = api_tag.findall(api_root[0].get("Body"))
print(allmatches)
##print(match_obj.string[match_obj.start():match_obj.end()])

##for row in api_root.findall("row"):
##    body = row.get("Body")
##    pos = 0
##    match_obj = api_tag.search(body, pos)
##    while pos < len(body) and (match_obj is not None):
####        prev = match_obj.string[:match_obj.start()]
####        mid = "<api>" + match_obj.string[match_obj.start(): match_obj.end()] + "</api>"
####        last = match_obj.string[match_obj.end():]
####        body = prev + mid + last
##        api_set.add(match_obj.string)
##        count += 1
##        pos = match_obj.end();
##        match_obj = api_tag.search(body, pos)

##    row.set("Body", body)

print(count)
print(api_set)

