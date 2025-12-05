import re
pattern = r"a.*b$"
pattern1 = r"^(?!.*z.*z).*$"
str1 = "ajghb"
str2 = "enzo fernandes"
if re.search(pattern1,str2):
    print("Found")
else:
    print("Not Found")
'''matches = re.findall(pattern,"LXI2013 VXI2015 VDI20104 Maruti Suzuki Cars in India") #list of match objects
print(matches)
for match in matches:
    print(match,end= " ")
str1="abbd"
regex = r"^(.).*\1$"
if re.findall(regex,str1):
    print("Valid")
else:
    print("Invalid")'''
