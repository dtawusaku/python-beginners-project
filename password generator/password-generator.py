# Import libraries
from operator import length_hint
import random
import string

# Getting to know the string function
    # a = string.digits
    # b = string.ascii_letters
    # c = string.ascii_lowercase
    # d = string.ascii_uppercase
    # e = string.punctuation
    # f = string.hexdigits

# getting random numnbers with range
    # t = random.randrange(2,10)

# prompt message
print("Welcome!")
# get length
length  = int(input("Enter the length of the password to be generated:"))
# process stage
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
syms = string.punctuation
# Using the .sample function
all = lower + upper + num + syms
temp = random.sample(all,length)
password = "".join(temp)
# display generated password
print("Length:" + str(length))
print("Password:" + password)