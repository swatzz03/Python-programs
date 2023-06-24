#1.Get an integer input from a user.If the number is odd,then find the factorial of a number and find the number of digits in the factorial of the number.If the number is even,then check the given is palindrome or not.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    # Convert the number to a string and check if it's equal to its reverse
    return str(n) == str(n)[::-1]

# Get input from the user
number = int(input("Enter an integer: "))

if number % 2 != 0:  # Odd number
    # Calculate the factorial of the number
    fact = factorial(number)

    # Calculate the number of digits in the factorial
    num_digits = len(str(fact))

    print("Factorial of", number, "is:", fact)
    print("Number of digits in the factorial:", num_digits)

else:  # Even number
    if is_palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")


#2.Given two strings,print (yes or no) whether the second string can be obtained from the first by deletion of none,one or more characters.

str1=str(input("Enter the first string\n"))
str2=str(input("Enter the second string\n"))
str3=''
temp=0
len1=len(str1)
len2=len(str2)
for iter1 in range(0,len2):
    for iter2 in range(temp,len1):
        if(str2[iter1]==str1[iter2]):
            str3=str3+str1[iter2]
            temp=iter2+1
            break
if(str2==str3):
    print("yes,the second string can be obtained from the first one")
else:
    print ("no,the second string cannot be obtained from the first one")


#3.a).Programs for positive and negative indexing.


n=int(input("Enter number of elements in list "))
l=list()
for i in range(0,n):
    e=input("enter the value")
    l.append(e)
print ("Original list : " + str(l))
k=input("Enter the element to be searched in the lsit ")
res=len(l)-l.index(k)
print("The required Negative index : -",str(res))
print("The required Positive index : ",l.index(k))
'''res = ~l[::-1].index(k)
print("The required Negative index : ",str(res))'''

#3.b).programs to check if the given list is in ascending order or not.

n=int(input("Enter number of elements in list "))
l=list()
for i in range(0,n):
    e=input("enter the value")
    l.append(e)
print ("Original list : " + str(l))
flag = 0
'''i = 1
while i<len(l):
    if(l[i] < l[i - 1]):
        flag = 1
    i += 1'''
l1 = l[:]
l1.sort()
if (l1 == l):
    flag = 1
'''if (not flag) :
    print ("Yes the list is in ascending order.")
else :
    print ("No the list is not in ascending order.")'''

if (flag) :
    print ("Yes the list is in ascending order.")
else :
    print ("No the list is not in ascending order.")


#4.a) Python program to convert a tuple to a string.

def str1(t):
    res = ' '
    for item in t:
       res = res + item
    return res
n=int(input("Enter number of elements in tuple "))
l=list()
for i in range(0,n):
     e=input("enter the value:")
     l.append(e)
a=tuple(l)
print("The string is", str1(a))



#4.b)Python program to reverse a tuple


'''def rev(t):
    res = t[::-1]
    return res'''

def rev(t):
    res = ()
    for k in reversed(t):
        res = res + (k,)
    return res

n=int(input("Enter number of elements in tuple "))
l=list()
for i in range(0,n):
    e=input("enter the value:")
    l.append(e)
a=tuple(l)
print(rev(a))



#5.Python program to check if a set is a subset of another set.


setx = set(["apple", "mango",45,33,99])
sety = set(["mango", "orange",33])
setz = set(["mango"])
print("x: ",setx)
print("y: ",sety)
print("z: ",setz,"\n")
print("Checking whether X is subset of Y...... \n")
if(setx.issubset(sety)==True):
    print("The set X is the subset of set Y \n")
else:
    print("The set X is not the subset of set Y \n")
print("Checking whether Y is subset of X...... \n")
if(sety.issubset(setx)==True):
    print("The set Y is the subset of set X\n")
else:
    print("The set Y is not the subset of set X\n")
print("Checking whether Y is subset of Z...... \n")
if(sety.issubset(setz)==True):
    print("The set Y is the subset of set Z\n")
else:
    print("The set Y is not the subset of set Z\n")
print("Checking whether Z is subset of Y...... \n")
if(setz.issubset(sety)==True):
    print("The set Z is the subset of set Y\n")
else:
    print("The set Z is not the subset of set Y\n")


#6.Python program to iterate over dictionaries using for loops.


color = {}
n = int (input("Enter the number of elements:"))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    color[key]=value
print("Dictionary elements are:\n")
for key,value in color.items():
    print(key,value)



#7.a).NumPy Program to convert a list of numeric value into a one dimensional NumPy array.


import numpy as np
l = list(map(float, input("Type number with space: ").split()))
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)


#7.b).NumPy Program to convert a list and tuple into arrays.

import numpy as np
lst = list(map(float, input("Type number with space (list): ").split()))
print("Original List: ",lst)
print("List to array conversion: ")
print(np.asarray(lst))
tup= tuple(map(float, input("Type number with space (Tuple): ").split()))
print("Original Tuple: ",tup)
print("Tuple to array: ")
print(np.asarray(tup))


#8.a).Program to convert a NumPy array and series to data frames.

import numpy as np
arr = np.random.rand(3) 
print("Numpy array:")
print(arr)
#conversion of array to dataframe
import pandas as pd 
print("\nArray to DataFrame: ")
#conversion of array to series
series = pd.Series(arr)
print("Series:")
print(series)
# conversion of series to dataframe
df = pd.DataFrame({'A':series})
print("\nSeries to DataFrame:")
print(df)


#8.b).Programs to add,subtract,multiple and divide two pandas series.


import pandas as pd
ds1 = pd.Series([12, 45, 6, 81, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Addition of two Series:")
print(ds)
print("Subtraction of two Series:")
ds = ds1 - ds2
print(ds)
print("Multiplication of two Series:")
ds = ds1 * ds2
print(ds)
print("Division of Series1 by Series2:")
ds = ds1 / ds2
print(ds)



#8.c).Programs to retrive and manipulate data using data frames.


import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Eva'],
    'Age': [25, 32, 28, 41, 36],
    'Country': ['USA', 'Canada', 'UK', 'USA', 'Australia'],
    'Salary': [5000, 7000, 6000, 8000, 6500]
}

df = pd.DataFrame(data)

# Retrieve data from the DataFrame

# Access a single column
name_column = df['Name']
print("Name column:")
print(name_column)

# Access multiple columns
age_salary_columns = df[['Age', 'Salary']]
print("\nAge and Salary columns:")
print(age_salary_columns)

# Access a single row by index
row_2 = df.loc[2]
print("\nRow at index 2:")
print(row_2)

# Access a subset of rows using conditions
usa_rows = df[df['Country'] == 'USA']
print("\nRows with Country as USA:")
print(usa_rows)

# Manipulate data in the DataFrame

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(df)

# Update values in a column
df.loc[3, 'Age'] = 42
print("\nDataFrame with updated Age value:")
print(df)

# Delete a column
df.drop('Salary', axis=1, inplace=True)
print("\nDataFrame with Salary column deleted:")
print(df)






































































    




























    
    
