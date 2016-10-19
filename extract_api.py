import re
import json
import xml.etree.ElementTree as ET

api_pattern = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\([_a-zA-z0-9]*\)")

tree = ET.parse("Posts.xml")
root = tree.getroot()

f_post = open("Posts.json", "w+", encoding = 'utf-8')
f_api = open("APIs.json", "w+", encoding = 'utf-8')

for child in root:
    json_str = json.dumps(child.attrib, ensure_ascii = False)
    match_obj = api_pattern.search(child.get("Body"))
    if match_obj is not None:
        f_api.write(json_str + "\n")
    else:
        f_post.write(json_str + "\n")

f_api.close()
f_post.close()

