import re
import utilities

##recogniser = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\(+.*?\)+")


##api_tag = re.compile("<api>" + ".+?" + "</api>")
##api_tree = parsexml("../dataset/APIs_Fully_Annotated.xml")
##api_root = api_tree.getroot()
##api_set = set()

##for row in api_root.findall("row"):
##    allmatches = api_tag.findall(row.get("Body"))
##    api_set |= set(allmatches)
##    
##    
##print(len(api_set))
##print(api_set)

recogniser_tree = utilities.parsexml("../dataset/API_Sample.xml")
recogniser_root = recogniser_tree.getroot()

##print(recogniser_root[1].get("Body"))
##rec_all = recogniser.findall(recogniser_root[1].get("Body"))
##print(rec_all)

rec_all = []
count = 0
for row in recogniser_root.findall("row"):
    row_api = utilities.api_pattern.findall(row.get("Body"))
    rec_all.append(row_api)
    count += len(row_api)
    
print(count)

##f = open("apis.text", "a", encoding = "utf-8")
##for item in rec_all:
##    f.write(str(item) + "\n")
##f.close()
