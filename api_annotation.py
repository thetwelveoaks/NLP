import json
import re


api_pattern = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\(")

f_api = open("APIs.json", "r", encoding = "utf-8")
f_api_annt = open("APIs_Annotated.json", "a", encoding = "utf-8")
f_api_annt_h = open("APIs_Annotated_HR.json", "a", encoding = "utf-8")

count = 0

for line in f_api:
    api_dict = json.loads(line)
    pos = 0
    match_obj = api_pattern.search(api_dict['Body'], pos)
    while pos < len(api_dict['Body']) and (match_obj is not None):
        prev = match_obj.string[:match_obj.start()]
        mid = "<api>" + match_obj.string[match_obj.start(): match_obj.end() - 1] + "</api>"
        last = match_obj.string[match_obj.end() - 1: ]
        new_str = prev + mid + last
        api_dict['Body'] = new_str
        count += 1
        pos = match_obj.end();
        match_obj = api_pattern.search(api_dict['Body'], pos)

    f_api_annt.write(json.dumps(api_dict) + "\n")
    f_api_annt_h.write(json.dumps(api_dict, indent = 4) + "\n")
        
f_api.close()

print(count)
