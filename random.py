s=[]

def i(text):
    rpl= [":","=","&","*"]  #replacing def
    for c in text:
        if c in rpl:
            text = text.replace(c, r':')
            return text
e={"Age" : 30 ,"Meek" : "mehedi"}
text=input(print("Enter Key:value "))
e2=i(text)
e3 = e2.split(":")
print(e3)
e[e3[0]]=e3[1]
print(e)