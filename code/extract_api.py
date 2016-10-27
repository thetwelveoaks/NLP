from utilities import parsexml, api_pattern
import re

tree = parsexml("../Data_set/Posts_HTML_FREE.xml")
root = tree.getroot()

api_count = 0
for row in root.findall("row"):
    match_obj = api_pattern.search(row.get("Body"))
    if match_obj is None:
        root.remove(row)
    else:
        api_count += 1

tree.write("../Data_set/APIs.xml")

print(str(api_count) + " posts with at least one API extracted")

