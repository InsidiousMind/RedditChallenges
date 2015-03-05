from functools import reduce
print("Welcome to Insidious'Fancy Calculator")
print ("Enter 'q' to quit, '+', '-', '*', '/' are the operations")

def toInt(n): return map(lambda x: int(x), n)
def add(n): return reduce(lambda x,y: x+y, n)
def subt(n): return reduce(lambda x,y: x-y, n)
def mult(n): return reduce(lambda x,y: x*y, n)
def div(n): return reduce(lambda x,y: x/y, n)
def groupBy(c,myList):return reduce(lambda acc,x: acc+[[]] if x==c else acc[:-1]+[acc[-1]+[x]], myList,[[]])
def formNum(nums, char):
    nums = nums.split(char)
    nums = toInt(nums)
    return nums
#Main Loop
while True:
    numbers = input()
    if numbers == "q": break
    elif "*" and "+" and "-" in numbers:
        pass
        
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
        

