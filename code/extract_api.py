from utilities import parsexml, api_pattern, excep_pattern
import re

tree = parsexml("../dataset/Posts_HTML_FREE.xml")
root = tree.getroot()

api_count = 0
excep_limit = 10

for row in root.findall("row"):
    allmatches = api_pattern.findall(row.get("Body"))
    valid = True
    if not allmatches:
        root.remove(row)
        valid = False
    for match in allmatches:
        match_obj = excep_pattern.search(match)
        if match_obj is not None:
            if excep_limit > 0:
                excep_limit -= 1
            else:
                root.remove(row)
                valid = False
            break
    if valid:
        api_count += 1

tree.write("../dataset/APIs.xml")

print(str(api_count) + " posts with at least one API extracted")

