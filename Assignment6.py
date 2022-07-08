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


def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
if (found == False):
    print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))                

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

