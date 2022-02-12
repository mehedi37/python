import time
from random import randint
wish = ["🎂 Happy BirthDay!", "🍰", "🕯", "🌷sorry again forgot!", "💙 Many many happy returns of the day !"]
for i in range(1, 85):
    print(' ')
    space = ' '
for i in range(1, 100):
    count = randint(1, 1000)
    while(count > 0):
        space += ' '
        count -= 1
    if(i%2 == 0):
        print(space + wish[0])
    elif(i%5 == 0):
        print(space + wish[1])
    elif(i%4 == 0):
        print(space + wish[2])
    elif(i%3 == 0):
        print(space + wish[3])
    elif(i%6 == 4):
        print(space + wish[1])
    else:
        print(space + wish[1])
    space = ''
    time.sleep(0.2)
