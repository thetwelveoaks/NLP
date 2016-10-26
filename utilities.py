import xml.etree.ElementTree as ET
import re

def parsexml(path):
    tree = ET.parse(path)
    return tree

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

api_pattern = re.compile("[_a-zA-Z][_a-zA-Z0-9]*\.[_a-zA-Z][_a-zA-Z0-9]*\([_a-zA-z0-9\.+\-*/%]*\)")
