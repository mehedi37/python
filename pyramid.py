# You can do loop using this without really using loop statement !
# But it's preety messy. So, think twice !

def loop(n, r):
    if n > 0:
        loop(n-1, r)                # This will re-initialize the loop function till 0 is achieved
        print(" "*(r-n)+"* "*n)     # Only then this statement will trigger one by one !
                                    # Getting Headache ? Think again !

inputs = int(input("Rows : "))
loop(inputs, inputs)
