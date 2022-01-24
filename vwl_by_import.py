from meek import vwl
quit = ['',' ','!']

while(True):
	str1=input("Enter a string: ")

	if str1 in quit:
		break
	
	else:
		v = vwl.vl(str1)
		c = vwl.con(str1)
		print(f"\n Vowles : ",len(v),"\t\t",v,"\n Consunents : ",len(c),"\t",c)