import re
str1=input("Enter a string: ").lower()
vwl=re.findall('[aeiou]',str1)
cons=re.findall('[^aeiou]',str1)
print("Total vowel: ",len(vwl))
print("Total consonant: ",len(cons))