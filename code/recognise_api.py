import re
import utilities

##recogniser = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\(+.*?\)+")


api_tag = re.compile("<api>" + ".+?" + "</api>")
api_tree = utilities.parsexml("../dataset/APIs_Fully_Annotated.xml")
api_root = api_tree.getroot()
api_set = set()
total_api = 0

for row in api_root.findall("row"):
    allmatches = api_tag.findall(row.get("Body"))
    api_set |= set([utilities.trim_api_tag(api) for api in allmatches])
    total_api += len(allmatches)

##    count += len(allmatches)
    
##f = open("../workspace/apis.text", "a", encoding = "utf-8")
##for item in api_set:
##    f.write(str(item) + "\n")
##f.close()
##print(len(api_set))
##print(count)
##print(api_set)

recogniser_tree = utilities.parsexml("../dataset/API_Sample.xml")
recogniser_root = recogniser_tree.getroot()

##print(recogniser_root[1].get("Body"))
##rec_all = utilities.api_pattern.findall(recogniser_root[1].get("Body"))
##for api in rec_all:
##    api = "<api>" + api + "</api>"
##    if api not in api_set:
##        print("NO")
##print(rec_all)
##count = 0



##rec_all = []

rec_set = set()

for row in recogniser_root.findall("row"):
    rec_set |= set(utilities.api_pattern.findall(row.get("Body")))

falsepos = len(rec_set.difference(api_set)) # match what should not be matched
falseneg = len(api_set.difference(rec_set)) # not match what should be matched

print(falsepos)
print(falseneg)
print(len(api_set))

##f = open("apis.text", "a", encoding = "utf-8")
##for item in rec_all:
##    f.write(str(item) + "\n")
##f.close()
