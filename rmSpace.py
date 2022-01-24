s=[]
i=0
def rmSpace(text):
    rpl= [",","\t","&"," "]  #replacing def
    for c in text:          # "c" is considered as a common word present in both "String" and "rpl"
        if c in rpl:
            text = text.replace(c, r'')
            text=text.replace(" ", "")  #final white space replacing
            return text