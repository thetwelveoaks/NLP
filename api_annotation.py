import json
import re

api_pattern = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\([_a-zA-z0-9]*\)")

f_api = open("APIs.json", "r+", encoding = "utf-8")


line = json.loads(f_api.readline())
print(line['Body'])

pos = 0
match_obj = api_pattern.search(line['Body'], pos)
while pos < len(line['Body']) and (match_obj is not None):
    prev = match_obj.string[:match_obj.start()]
    mid = "<api>" + match_obj.string[match_obj.start():match_obj.end()] + "</api>"
    last = match_obj.string[match_obj.end():]
    new_str = prev + mid + last
    line['Body'] = new_str
    pos = match_obj.end();
    match_obj = api_pattern.search(line['Body'], pos)

print(line['Body'])

##for line in f_api:
##    line = json.loads(line)
    

f_api.close()
