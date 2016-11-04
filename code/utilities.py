import xml.etree.ElementTree as ET
import re

def parsexml(path):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse(path, parser)
    return tree

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def trim_api_tag(api):
    return api.replace("<api>", "").replace("</api>", "")

api_pattern = re.compile("([\$_a-zA-Z][\$_a-zA-Z0-9]*?\.)+[\$_a-zA-Z][\$_a-zA-Z0-9]*\(.*?\)+")
excep_pattern = re.compile("\([_a-zA-Z][_a-zA-Z0-9]*\.java:[0-9]+?\)")
