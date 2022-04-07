# Task 1


# # importing libraries
# import time as t

# # Prints hello world after 10 seconds
# t.sleep(10)
# print("Hello World")


# Task 2

import time as t
def countdown(tme):
    print("This window will remain open for " + str(tme) + " more seconds...")
    while tme >= 0:
        print(tme, end=' .  .  . ')
        t.sleep(1)
        tme -= 1
        print('Goodbye!!!! \n')
tme  = int(input("Enter number of seconds"))
countdown(tme)