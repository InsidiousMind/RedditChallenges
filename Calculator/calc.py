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
    nums = re.split(r'[+ - * / \s]\s*', nums)
    for item in nums: item.strip()
    nums = filter(None, nums)
    nums = toInt(nums)
    return nums
#Main Loop
while True:
    numbers = input()    
    if numbers == "q": break
    s = ["*", "-", "/", "+"]
    count = 0
    for item in numbers:
        if item in s:
            count += 1
            s.remove(item)
    if count > 1: print("Can't do that operation, sorry. This Calculator doesn't know PEMDAS")
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

