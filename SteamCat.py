import re

unparsedHTML = open("unparsed.txt", "r", encoding="utf8")#Opens file containing unparsed AppIDs in HTML
toParse = unparsedHTML.read()
parsed = re.findall("/app/(\\d*)", toParse)#Parses file for all AppIDs, stores as list

storedAppIDs = open("addToVDF.txt", "a")
category = input("Enter a name for this category:")
numberAssigned = str(len(parsed))
for x in parsed:
    storedAppIDs.writelines(["\t\t\t\t\""+x+"\"\n", "\t\t\t\t{\n", "\t\t\t\t\t\"tags\"\n", "\t\t\t\t\t{\n", "\t\t\t\t\t\t\"0\"\t\""+category+"\"\n", "\t\t\t\t\t}\n", "\t\t\t\t}\n"])#Formatting for VDF
print("Assigned "+numberAssigned+ " items to "+category)