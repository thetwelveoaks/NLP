import re
import utilities

api_tag = re.compile("<api>" + ".+?" + "</api>")
api_tree = utilities.parsexml("../dataset/APIs_Fully_Annotated.xml")
api_root = api_tree.getroot()
api_set = set()

# Get annotated API mentions
for row in api_root.findall("row"):
    allmatches = api_tag.findall(row.get("Body"))
    api_set |= set([utilities.trim_api_tag(api) for api in allmatches])

recogniser_tree = utilities.parsexml("../dataset/API_Sample.xml")
recogniser_root = recogniser_tree.getroot()
rec_set = set()

# Recognise API mentions
for row in recogniser_root.findall("row"):
    iterator = utilities.api_pattern.finditer(row.get("Body"))
    for match in iterator:
        temp = []
        temp.append(match.group())
        rec_set |= set(temp)
##    rec_set |= set(utilities.api_pattern.findall(row.get("Body")))

# Compute false positives and false negatives
falsepos = len(rec_set.difference(api_set)) # match what should not be matched
falseneg = len(api_set.difference(rec_set)) # not match what should be matched

print("False Positives: " + str(falsepos))
print("False Negatives: " + str(falseneg))
print("Total unique APIs: " + str(len(api_set)))

f_falpos = open("../dataset/falpos.txt", "w", encoding = 'utf-8')
for api in rec_set.difference(api_set):
    f_falpos.write(str(api) + "\n")
f_falpos.close()

f_falneg = open("../dataset/falneg.txt", "w", encoding='utf-8')
for api in api_set.difference(rec_set):
    f_falneg.write(str(api) + "\n")
f_falneg.close()


