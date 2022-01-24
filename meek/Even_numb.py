# For loop without List 

count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        count+=1
print(f"We have {count} even numbers")



# with while  and list 
evens = [2,4,6,8]
count = 0
n = 1
while (n<=10):
    if n in evens:
        print(n)
        count+=1
    n+=1
print(f"We have ",count,"Even Numbers")


# while without list 

n=1
count=0
while(n<=4):
    even=n*2
    print(even)
    count+=1
    n+=1
print(f"We have ",count," evens here")


# For loop and list 
evens = [2,4,6,8]
count = 0
for x in range(1,10):
    if x in evens:
        count+=1
        print(x)
print(f"We have ",count," even numbers")