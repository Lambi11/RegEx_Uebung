import re

txt = 'The rain in Spain'
x = re.search('ai', txt)
print(x)

txt = 'The rain in Spain'
x = re.findall('ai', txt)
print(x)