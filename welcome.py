def loop(r, c):
    rwMid = (r-1)//2
    for i in range(r):
        reBefore = int(c-3*(2*i+1))         # For Odd series
        reAfter = int(c-3*(2*(r-i)-1))      # Doing (r-i) for reverseing the same upper thing
        remWelcome = int(c-7)               # Welcomes constant length is 7. That's why
        if (i < rwMid):
            print("-"*(reBefore//2) + "•|•"*(2*i+1) + "-"*(reBefore//2))
        elif (i == rwMid):
            print("-"*(remWelcome//2) + "WELCOME" + "-"*(remWelcome//2))
        elif (i > rwMid):
            print("-"*(reAfter//2) + "•|•"*(2*(r-i)-1) + "-"*(reAfter//2))  # Doing -1 because (r-i) will not go till 0 it will go till 1
inputs = int(input("Rows : "))
loop(inputs, inputs*3)
