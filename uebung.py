import re

txt = "Ich habe 1 Präsentation zum Thema REGEX erstellt"
result = re.search(r"(\b\d+).+(\b[A-Z]+\b)", txt)
print(result.groups()) 
print(result.group(1))
print(result.group(2))


#Benutzer E-Mail
pattern = "[(a-z)(A-Z)(0-9)]+@[(a-z)(A-Z)]+\.(com|de)"
user_input = input('Enter your email: ')
if(re.search(pattern, user_input)):
    print('valid email')
else:
    print('invalid email')    