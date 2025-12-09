# Python Loop problems

# You are given a number N, you need to print its multiplication table.
def multiplicationTable(N):
    for i in range(1, 11):
        print(N*i, end=" ")

# You are given a string s, you need to print its characters at even indices(index starts at 0).
def stringJumper(s):
    for i in range(0,len(s), 2):
        # from 0 to length of str and skip 2
        print(s[i], end="") #DcoPeoea
        #printing character and separating characters by nothing


# While loop - Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line.
def printInDecreasing(x):
    # code here
    
    while (x >= 0):
        print(x,end=" ")
        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code

        x -= 1

# Jumping throgh while - Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
def printIncreasingPower(x):
    i=1#code here
    while(i<=x):
        pow = i**2
        if(pow<=x):
            print(pow, end = " ")
        i+=1

# Zero Converter = You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
def pos(n):
    ## Write the code
    if n>=0:
        if(n == 0):
         return "already zero"
        else:
           n-=1
           while(n >= 0):
              print(n, end=" ")
              n -= 1
def neg(n):
    ##Write the code
    if n<0:
        while(n <= 0):
           print(n, end=" ")
           n += 1

# The Else Statement -You have to take an interger input a, and then use the if statement to print "Big" (without quotes) if the given number is greater than 100, and use the else statement to print "Number" (without quotes) when the number is smaller than or equal to 100.
a = int(input())

if a > 100:
    print("Big")
else:
    print("Number")

# Function With Return Value - Here one integer n is given. You need to write the complete function returnValueFunction that takes n as a parameter and uses the return keyword to return double the value of n.
def returnValueFunction(n):

  return n * 2


# Function With No Arguments - This problem has no input. You need to write the function helloFunction that prints Hello.

def helloFunction():

  print("Hello")


# Function With Arguments - Here two integers a and b are given. The given input and its values are passed as arguments to the function argumentFunction. The argumentFunction is responsible to return (a+b). You need to write this function.
def argumentFunction(a, b):

  return (a+b)

# First Digit of a Number- Given a number n, find the first digit of the number..
def firstDigit(n):
    #code here
      #code here
    x = str(n)
    return int(x[0])

# Print GFG n times - Print GFG n times without the loop.
class Solution:
    def printGfg(self, n):
        # Code here
        if n<1:
            return
        print("GFG", end=' ')
        self.printGfg(n-1)
        

