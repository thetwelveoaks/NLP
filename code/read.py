import utilities

tree = utilities.parsexml("../APIs_Annotated.xml")
root = tree.getroot()
print(root[0].get("Body"))
