# __int__(vwl) = __main()__
import re
def vl(text):
	vwl=re.findall('[aeiou]',text.lower())
	return vwl


def con(text):
	cons=re.findall('[bcdfghjklmnpqrstvwxyz]',text.lower())
	return cons											