import re

#txt = 'The rain in Spain'
#x = re.search('ai', txt)
#print(x)

#txt = 'The rain in Spain'
#x = re.findall('ai', txt)
#print(x)

txt = "Ich habe 1 Präsentation zum Thema REGEX erstellt"
result = re.search(r"(\b\d+).+(\b[A-Z]+\b)", txt)
print(result.groups()) 
print(result.group(1))
print(result.group(2))