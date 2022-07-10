#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#Q1

def perfect_no(num):
    #Make a loop to find the divisors of the number and add them
    sum_of_divisor = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            sum_of_divisor += divisor
    
    if (sum_of_divisor/2) == num:
        return f"{num} is a perfect number"
    else:
        return f"{num} is not a perfect number"

user_input = int(input("Enter number you want to check\n"))
print(perfect_no(user_input))


# In[ ]:
#Q2

def palindrome(user_inp):
    #remove the spaces in the input string
    joined = user_inp.replace(" ", "")
    reverse_str = joined[::-1]
    
    if reverse_str == joined:
        return "Yes, the entered string is a palindrome"
    else:
        return "No, the entered string is not a palindrome"

user_inp = input("Enter string to check\n")
print(palindrome(user_inp))

# In[ ]:
#Q3

from math import factorial

from math import factorial
def pascal_triangle(n):
    for i in range(n):
        for j in range(n-1-i):
            print(" ", end="")
        for k in range (i+1):
            print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
        print()

n=int(input("Enter no of rows: "))
pascal_triangle(n)

# In[ ]:
#Q4

def palgram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str:
            return False
    return True

user_string=str(input("Enter a sentence: "))
if palgram(user_string)==False:
    print("entered sentence is not a palgram")
else:
    print("entered sentence is palgram")


# In[ ]:
#Q5

def sort_alpha():
    seq = input("Enter a hyphen-separated sequence of words: ")
    a = seq.split("-")
    b = sorted(a)
    c = "-".join(b)
    print(c)
sort_alpha()


# In[ ]:
#Q6

def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Aayush","Mechanical",21107001)


# In[ ]:
#Q7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("Check whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()


# In[ ]:
#Q8

class Zero:
    def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(Zero().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))                 

# In[ ]:
#Q9

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")

