print("--------------Program 1-------------------")

# 1 . Implement palindrome using iterator(for loop) and generator mechanism.

# Using For loop :
num = input("Enter the number :")  # giving user input number
i = 0  # initializing i =0
for i in range(len(num)):  # using for loop for i to length of number
    if num[i] != num[-1 - i]:  # checking for given condition if satisfies num is not a pal else num is a pal
        print(num, "is not a palindrome")
        break
    else:
        print(num, "is a palindrome")
        break

# Using generator mechanism :
num1 = input("Enter any number : ")
for i in range(len(num1)):
    if num1 == num1[::-1]:
        print(num1, "is a palindrome")
        break
    else:
        print(num1, "is not a palindrome")
        break


print(-----------------Program-2--------------------)
""" 
2 .   Sum of 2 digits into output
 		n1 = 1234 # int(input("Enter number1 :" ))
 		n2 = 9999 # int(input("Enter number2 :" ))
 		Output: 9+1 2+9 3+9 4+9
 		         10 + 11 + 12 + 13
 				 46
"""

n1 = int(input("Enter number-1 : "))    #User input-1
n2 = int(input("Enter number-2 : "))    #User input-2
print("number-1", n1)
print("number-2", n2)


def s(n):   #defining a function
    sum1 = 0    #initializing sum=0
    d = 0
    for i in range(len(str(n))):    #for loop with range and checking modules and floor division
        d = n % 10
        sum1 = sum1 + d
        n = n // 10
    return int(sum1)    #returning sum1


d_n1 = s(n1)
d_n2 = s(n2)

print(d_n1 + d_n2)  #printing total sum





print(-------------------Program-3-------------------------)
"""
3. st = "ab@#cd!ef"
Reverse string considering only alphabets. Symbols should not be reversed
"""
Ans :
strSample = "ab@#cd!ef" #given string
print("String before reversing :", strSample)

listSample = list(strSample)    #converting string into list

i = 0
j = len(listSample) - 1

while i < j:    #while loop with if elif else conditions
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1
strOut = ''.join(listSample)
print("string after reversing only alphabets", strOut)




print(----------------Program-4--------------)
"""
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
findout elements duplicate count output in  dict format

"""
Ans:
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]  #given list
dict1 = {}  #creating empty dictionary
for ele in some_list:
    dict1[ele] = some_list.count(ele)

print("No of element duplicates count are:", dict1)


print(---------------Program-5---------------------)
"""
5. # t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")

"""

t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
l1 = [] #creating empty list
c1 = [] #empty list
for i in t1:
    if type(i) == int:  #checking type of element
        l1.append(i)    #if int its appending to l1
    else:
        c1.append(i)    #if not int appending to c1
l2 = []
c2 = []
for i in t2:
    if type(i) == int:
        l2.append(i)
    else:
        c2.append(i)
l3 = []
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
c3 = []
for i in range(len(c1)):
    c3.append(c1[i]+c2[i])
print(l3 + c3)



print(------------------Program-6---------------------)
"""6 Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			o/p =  216.8.94.196"""
Ans :
def remove_zeros(ip):   #defining function
    new_ip = ".".join([str(int(i)) for i in ip.split(".")]) #list comprehension with join function
    return new_ip

ip = "216.08.094.196"
print(remove_zeros(ip))



print(------------------------Program-7--------------------)
"""
7. l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
#output= [1,2,3,4,5,6,7,8,9,10]
"""
Ans :

l = [1,2,[3,4],[5,6],7,[8,9,10]]
new_list = []   #empty list
[new_list.extend(x) if type(x) is list else new_list.append(x) for x in l]  #list comprehension with condition
print(new_list)



print(--------------------Program-8-----------------------)
"""
8. Load sample content in text file.
   Read data and find
    1. No of lines in file
	2. No of words in each line 
	3. No of chars in each line
	4. No of vowels and consonants
	5. No of special chars linewise and total 
"""
Ans :

# open file in read mode

"""No of lines in a file"""
with open(r"C:\python.txt", 'rt') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)

"""No of words in each line"""
file = open(r"C:\python.txt", "rt")
python = file.read()
words = python.split()
print('Number of words in text file :', len(words))

"""No of characters in each line"""
file = open(r"C:\python.txt", "r")
data = file.read()
number_of_characters = len(data)

print('Number of characters in text file :', number_of_characters)

"""Number of the vowels in file"""
file = open(r"C:\python.txt", "r")
str1 = file.read()
vowel_count = 0
cons_count = 0
for i in str1:
    if (i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I'
            or i == 'i' or i == 'O' or i == 'o'
            or i == 'U' or i == 'u'):
        vowel_count += 1
    else:
        cons_count += 1

print('The Number of Vowels in text file :', vowel_count)
print('The Number of Consonants in the text file : ', cons_count)

""" No of special chars linewise and total """

count_special = 0
with open(r"C:\python.txt", 'rt') as fp:
    for line in fp:
        count_special += sum(not x.isalnum() for x in line)
print("No of special characters are :", count_special)
