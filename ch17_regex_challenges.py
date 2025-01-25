import re

text = "The Zen of Python"
m = re.findall("Dutch", text)
##for each in m:
##    print(each)

text2 = """Arizona 479, 501, 870. California 209, 213, 650."""
m = re.findall("\d+", text2)
# print(m)
##for each in m:
##    print(each)

text3 = "The ghost that says boo haunts the loo."
matches = re.findall(".oo", text3, re.IGNORECASE)
for match in matches:
    print(match)
  
