from utilities import parsexml, cleanhtml


tree = parsexml("../Data_set/Posts.xml")
root = tree.getroot()

for row in root.findall("row"):
    body = cleanhtml(row.get("Body"))
    row.set("Body", body)

tree.write("../Data_set/Posts_HTML_FREE.xml")
