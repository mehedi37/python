line=int(input("\n Enter Rows : "))
if line<100 and line>1:				  #Ensures Limited value !
    elmnt=[]
    for i in range (0,line):
        cl=input("\n Eliments : ")
        elmnt.append(cl)
        if (len(elmnt[0])==len(elmnt[i])):		# varification of being matrix
            clv=int(cl)		# varification of eliments value is Intiger
            if (len(cl)==line):
                x=1
                i=0
                i+=i
            else:
                x=0
        else:
            x=0
            print("\n\n Not A Matrix ! \n\n Reasons: \n 1)You've Entered Extra or Less Numer of values than the previous input ! \n 2)NOT INTIGER values !")
            break
    if x == 1:
        print("\n Yes")
    else:
        print("\n No")
else:
	print("Lol ! Out of range !")
