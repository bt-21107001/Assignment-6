#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def perfect(num):
    num_div=[]
    sum=0

    for i in range(1,num+1):
        if num%i==0:
            num_div.append(i)
    print("divisors of ", num," are ", num_div)

    for elem in num_div:
        sum= sum+elem
    if num==0.5*sum:
        print(num, " is a perfect number.")
    else:
        print(num, " is not a perfect number.")

num= int(input("enter a number to check whether its perfect: "))
perfect(num)


# In[ ]:


def palindrome(string):
    rev_string=string[::-1]
    if string==rev_string:
        print("entered string is a palindrome")
    else:
        print("entered string is not a palindrome")

user_string=str(input("enter a word, phrase or sentence: "))
palindrome(user_string)


# In[ ]:


from math import factorial

n=int(input("Enter no of rows: "))
for i in range(n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range (i+1):
        print(factorial(i) // (factorial(i-k)*factorial(k)) , end=" ") # nCr = n! / ((n-r)! * r!)
    print()


# In[ ]:


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


input_string=str(input("enter a hyphen separated sentence: "))

li=list(input_string.split("-"))
li.sort()

print("-".join(li))


# In[ ]:


def student_data(student_name , student_branch, student_id):
    print("student name: ",student_name)
    print("student branch: ",student_branch)
    print("student id: ",student_id)

student_data("Aayush","Mechanical",21107001)


# In[ ]:


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

