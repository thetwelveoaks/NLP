from utilities import parsexml, cleanhtml


tree = parsexml("../dataset/Posts.xml")
root = tree.getroot()

for row in root.findall("row"):
    body = cleanhtml(row.get("Body"))
    row.set("Body", body)

tree.write("../dataset/Posts_HTML_FREE.xml")
