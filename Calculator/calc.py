from functools import reduce
import re

print("Welcome to Insidious' Fancy Calculator")
print ("Enter 'q' to quit, '+', '-', '*', '/' are the operations")

def toInt(n): return map(lambda x: int(x), n)
def add(n): return reduce(lambda x,y: x+y, n)
def subt(n): return reduce(lambda x,y: x-y, n)
def mult(n): return reduce(lambda x,y: x*y, n)
def div(n): return reduce(lambda x,y: x/y, n)

def formNum(nums, char):
    nums = nums.split(char)
    nums = toInt(nums)
    return nums
#Main Loop
while True:
    numbers = input()    
    if numbers == "q": break
    s = ["*", "-", "/", "+"]
    temp = re.split(r'[\d\s]\s*', numbers)
    count = 0
    for item in temp:
        if item in s:
            count += 1
            s.remove(item)
    if count > 1: 
        print("Can't do that operation, sorry. This Calculator doesn't know PEMDAS")
    elif "*" in numbers: 
        numbers = formNum(numbers, "*")
        print(mult(numbers))
    elif "+" in numbers:
        numbers = formNum(numbers, "+")
        print(add(numbers))
    elif "/" in numbers:
        numbers = formNum(numbers, "/")
        print(div(numbers))
    elif "-" in numbers:
        numbers = formNum(numbers,"-")
        print(subt(numbers))
    else:
        print("Probably can't do this operation, X.X")

