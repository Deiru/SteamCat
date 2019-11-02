import re

unparsedHTML = open("unparsed.txt", "r", encoding="utf8")#Opens file containing unparsed AppIDs in HTML
toParse = unparsedHTML.read()
parsed = re.findall("/app/(\\d*)", toParse)#Parses file for all AppIDs, stores as list

storedAppIDs = open("addToVDF.txt", "a")
category = input("Enter a name for this category:")
for x in parsed:
    storedAppIDs.writelines(["\""+x+"\"\n", "{\n", "\t\"tags\"\n", "\t{\n", "\t\t\"0\"\t\""+category+"\"\n", "\t}\n", "}\n"])#Formatting for VDF