import re
from utilities import parsexml, regex

recogniser = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\([_a-zA-z0-9\.+\-*/%]*(,[_a-zA-z0-9\.+\-*/%]*)*\)")
api_tag = re.compile("<api>" + ".+?" + "</api>")

api_tree = parsexml("../dataset/APIs_Fully_Annotated.xml")
api_root = api_tree.getroot()
api_set = set()

##allmatches = api_tag.findall(api_root[0].get("Body"))
##print(allmatches)
##print(match_obj.string[match_obj.start():match_obj.end()])

for row in api_root.findall("row"):
    allmatches = api_tag.findall(row.get("Body"))
    api_set |= set(allmatches)
    
    
print(len(api_set))
##print(api_set)

