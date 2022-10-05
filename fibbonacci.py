import time

def fibbonacci():
    goal = input("Enter an integer")
    try:
        goal = int(goal)
        x = 0
        y = 1
        if x == goal or y == goal:
            print("That's a fibbonacci number!")
        while y < goal:
            z = y
            y = x+y
            x = z
        if y == goal:
            print("That's a fibbonacci number!")
        else:
            print("That isn't a fibbonacci number")
    except: 
        print("That wasn't an integer")
        fibbonacci()
    
def x_fib_number(max):
    count = 1
    #max = input("Which fibbonacci number do you want?")
    try:
        max = int(max)
        x = 0
        y = 1
        if max ==0:
            print(0)
        elif max == 1:
            print(1)
        else:
            while count < max:
                z = y
                y = x+y
                x = z
                count +=1
            print(y)
    except: 
        print("That wasn't an integer")
        x_fib_number()



#fibbonacci()
#x_fib_number(8)
