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
        

# List Traversal
# You are given a list that contains integers. You need to print the elements of the list with a space between them.
def listTraversal(arr):
    #code here
    for i in arr:
        print(i, end=" ")


# Length of The List
# You are given a list that contains integers. You need to return the length of the list.
def listLength(arr):
    return(len(arr))#output:5

# Sum The List : You are given a list that contains integers. You need to return the sum of the list.
def listSum(arr):
    #code here
    # return sum(arr)
    sum = 0
    for i in arr:
        sum += i
    return sum
    

# Decrement List Values : You are given a list that contains integers. You need to decrement each element of the list by 1 and return the list.
def decrementList(arr):
    #code here
    list=[]
    for i in arr:
        j=i-1
        list.append(j)
    return list

# Append To List
# You are given three inputs a, b, c. You need to create a list and append a, b, c to the list and then return that list.
def appendToList(a,b,c):
    #code here
    return [a,b,c]


# Less Than - You are given a number k and a list arr[] that contains integers. You need to return list of numbers that are less than k.
def lessThan(arr, k):
    #code here
    ans = [i for i in arr if i<k]
    return ans #2 1 5


# Average - You are given a list arr that contains integers. You need to return average of the non negative integers.
def nonNegativeAverage(arr):
    
    li = [i for i in arr if i>=0]
    avg = sum(li)/len(li)
    return avg


# Repeat the Strings - Python
# Given two strings a and b. The task is to make a new string where the string with longer length should be in between and the one with shorter length should be outside on front and end. New string should be like shorter+longer+shorter.
# Function to join given strings
def combo_string(a, b):

    # your code here
    short = a
    longer = b
    if(len(a) > len(b)):
      short = b
      longer = a
    return short + longer + short # forkpythonfork

# String Functions I - Python
# In this question, we'll take a look at inbuilt string methods like title(), swapcase(), find(), strip().
def trim(str):
     return str.strip()

def exists(str, x):
    return str.find(x)

def titleIt(str):
    return str.title()

def casesSwap(str):
    return str.swapcase()

# hello
# 2
# Hello
# HELLO

# Convert String to LowerCase : Given a string s. The task is to convert string characters to lowercase.
class Solution:
    def toLower (self , s : str)-> str :
        #code here 
        return s.lower() #abcdde
    
# Reverse String : Given a string s, you need to reverse it.
    # def reverseString(s):
    # #code here
    # result = ""
    # for i in range(len(s) - 1, -1, -1):
    #     result = result + s[i]
    # return result #olleH

# Check Palindrome : Given a string s, you need to check if it is palindrome or not. A palidrome is a string that reads the same from front and back.
def isPalindrome(s):
    #code here
    if s.lower() == s[::-1].lower():
        return True
    else:
        return False
    # False


# Find Pattern
# Given a string s, and a pattern p. You need to find if p exists in s or not and return the starting index of p in s. If p does not exist in s then -1 will be returned. Here p and s both are case-sensitive.
def findPattern(s,p):
    #code here
       for i in range(0, len(s) - len(p) + 1):
        if s[i:i + len(p)] == p:
            return i
        return -1 #2
       
# Decimal number to binary number
# Given a decimal number n (positive) in string format, compute its binary string equivalent and return it.
def toBinary(n):
    #Your code here
    binary = ""
    while n > 0:
        binary += str(n%2)
        n = int(n/2)
    return binary[::-1] 