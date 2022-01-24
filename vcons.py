import re
quit = ['',' ','!']
while(True):
	str1=input("\n Enter a string: ").lower()
	if str1 in quit:
		break
	elif str1.isalpha():
		vwl=re.findall('[aeiou]',str1)
		cons=re.findall('[^aeiou]',str1)
		print("Total vowel: ",len(vwl))
		print("Total consonant: ",len(cons))
	
	else:
		print("\n Enter Alphabets Only !")
