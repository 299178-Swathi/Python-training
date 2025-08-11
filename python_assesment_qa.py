# Python Coding Assessment (Hard Level)
# ________________________________________
# 🧠 Set 1: Balanced Assessment
# 1.	Sum of Positive Numbers Until Zero
# Take integer inputs from the user until they enter 0. Print the sum of only positive numbers.
# 🔹 [Basics, int, input/output, while loop, if]

# total=0
# while True:
#     num=int(input('enter any number'))
#     if num == 0:
#         break
#     elif num>0:
#         total=total+num
# print('sum of positive numbers:',total)



# 2.	Student Grade Classifier (if-elif-else)
# Input 3 subject marks. Use if-elif-else to assign grade:
# o	≥90 → A
# o	75-89 → B
# o	60-74 → C
# o	<60 → F
# 🔹 [float, avg, conditional logic]

sub1 = int(input('enter the marks scored science:'))
sub2 = int(input('enter the marks scored in mathematics:'))
sub3 = int(input('enter the marks scored in english:'))

avg = (sub1 + sub2 + sub3) / 3
if avg >= 90:
    print('you have scored grade A')
elif (avg < 90) or (avg >= 80):
    print('you have scored grade B')
elif (avg < 80) or (avg >= 70):
    print('you have scored grade C')
elif (avg < 70) or (avg >= 60):
    print('you have scored grade D')
elif (avg < 60) or (avg >= 40):
    print('you have scored grade E')
else:
    print('you have failed,reattempt')

#
#  3.	Tuple Processor
# Given a list of tuples like [(10, 2), (5, 0), (8, 4)], divide first by second only if second is not zero.
# 🔹 [tuple, list, loop, if]
# data=[(10, 2), (5, 0), (8, 4)]
# for a,b in data:
#     if b!=0:
#         result=a/b
# print(result)

#4.	Flatten Nested Dictionary (1 level)
# Given a dictionary like:
#  	data = {"a": 1, "b": {"x": 2, "y": 3}}
#  	Output: {"a": 1, "b.x": 2, "b.y": 3}
# 🔹 [dict, nested access, flattening logic]

# 5.	Hollow Pyramid Pattern with Numbers
# Input = 5
# Output:
#
#  	  1
#    1 2
#   1   3
#  1     4
# 1 2 3 4 5
#  	🔹 [nested loops, conditionals, spacing]

# rows=int(input('enter the number of rows'))
# for i in range(1, rows + 1):
#     print(' '*(rows-i),end='')
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == rows:
#             print(j,end=' ')
#         else:
#             print(' ',end=' ')
#     print()


# ________________________________________
# 🧠 Set 2: Balanced Assessment
# 1.	Calculate BMI
# Take height and weight from user, compute BMI = weight / height², and print result.
# 🔹 [float, input/output, basic operators]

# height=float(input('enter your height in meters:'))
# weight=float(input('enter your weight in kgs:'))
# BMI=weight/height**2
# print(f'Your BMI is:{BMI:}')
# if BMI<18.5:
#      print('Your are underweight')
# elif 18.5<=  BMI<24.5:
#      print('You have normal weight')
# elif 24.5<= BMI <29.5:
#      print('you are over weight')
# else:
#      print('You are obese')

# 2.	Odd-Even Counter in List
# Given a list, count how many numbers are odd vs even.
# 🔹 [list, int, loop, if-else, bool]

# l1=[22,56,34,79,67,54,23,13,45,32]
# even=[]
# odd=[]
# for i in l1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# l2=len(even)
# l3=len(odd)
# print(even)
# print(odd)
# print(l2)
# print(l3)
# 3.	Login Validation (nested if)
# Input username and password.
# o	If username is correct:
# 	Check password
# 	Else invalid password
# o	Else invalid user
# 🔹 [nested if, bool]

# user_name='swathi456'
# password='shashi123'
#
#
# a=input('enter username ')
# b=input('enter you password ')
# if a and b == user_name and password:
#     print('enter password')
# else:
#     print('invalid user')

# 4.	Flatten Dictionary with Mixed Types
# Input:
#  	{"x": 10, "y": {"a": 5, "b": {"z": 1}}}
#  	Output:
#  	{'x': 10, 'y.a': 5, 'y.b.z': 1}
#  	🔹 [recursion, nested dicts, keys handling]
# 5.	Hourglass Star Pattern
# Input = 5
# Output:
#  	*********
#  *******
#   *****
#    ***
#     *
#    ***
#   *****
#  *******
# *********
#  	🔹 [nested loops, symmetry, spacing]

# n=int(input('enter the number of rows'))
# for i in range(n, 0, -1):
#     print(' '*(n-i) + "* " * i)
#
# for i in range(2, n + 1):
#     print(' '*(n-i) + "* " * i)
# ________________________________________
# 🧠 Set 3: Balanced Assessment
# 1.	Add Two Floats and Print Boolean
# Input two float values. Print True if their sum > 100, else False.
# 🔹 [float, bool, input, if-else]
# a1=float(input('enter the first number'))
# b1=float(input('enter the second number'))
# c1=a1+b1
# if c1>100:
#     print(True)
# else:
#     print(False)
#
#2.	Reverse List Manually
# Input a list of integers and reverse it manually (no slicing).
l2=[12,34,45,78,'swathi','shashi',-78,46.8,3+4j]
l3=[]
for i in range (len(l2)-1,-1,-1):
    l3.append(l2[i])
print('reverse list is:',l3)



# 🔹 [list, loops, index handling]

# 3.	Leap Year Checker (if-elif-else)
# A year is leap if:
# o	Div by 4 and not by 100 or
# o	Div by 400
# 🔹 [int, conditionals]
# year=int(input('enter the year'))
# if (year%400 == 0) or (year%4 == 0 and year % 100 != 0):
#     print(year, 'is a leap year')
# else:
#     print(year, 'is not a leap year')


# 4.	Flatten List of Dicts to Single Dict
# Given:
#  	[{'a': 1}, {'b': 2, 'c': 3}, {'d': {'e': 4}}]
#  	Output: {'a': 1, 'b': 2, 'c': 3, 'd.e': 4}
# 🔹 [list, dict, flatten logic]
d1=[{'a': 1}, {'b': 2, 'c': 3}, {'d': {'e': 4}}]
fl= {}
for i in d1:
    if isinstance(i,dict):
        for key, value in i.items():
            if isinstance(value, dict):
                for k, j in value.items():
                    fl[f'{key}.{k}'] = j
            else:
                fl[f'{key}'] = value
print(fl)




# 5.	Diamond Star Pattern
# Input: 5
# Output:
#  	    *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#  	🔹 [nested loops, symmetry]

# n=int(input('enter the number of rows'))
# for i in range(1, n + 1):
#     print(' '* (n-i) +'* ' * i)
# for i in range(n - 1, 0, -1):
#     print(' '* (n-i) +'* ' * i)
# # ________________________________________
# 🧠 Set 4: Balanced Assessment
# 1.	Simple Calculator Using Operators
# Input two integers and an operator (+, -, *, /). Perform operation.
# 🔹 [int, operators, if-elif-else]
# print('enter your choice')
# print('for addition,choice 1')
# print('for subtraction choice 2')
# print('for multiplication choice 3')
# print('for division choice 4')
# choice=input('enter your choice 1,2,3,4:')
# a=int(input('enter first number'))
# b=int(input('enter the second number'))
# if choice == '1':
#     print(f'Result: ,{a}+{b}={a+b}')
# elif choice == '2':
#     print(f'Result: ,{a}-{b}={a-b}')
# elif choice == '3':
#     print(f'Result: ,{a}*{b}={a*b}')
# elif choice == '4':
#     print(f'Result: ,{a}/{b}={a/b}')
# else:
#     print('invalid choice')


# 2.	Float List: Avg > 60 Check
# Input N floats. Calculate average and check if > 60. Print True/False.
# 🔹 [float, list, loop, bool]

# n=[45.6,67,8,78.3,56.6,23.4,21.2,45]
# average=sum(n)/len(n)
# print('numbers:',n)
# print('Average: ',average)
# print(average>60)
#

# 3.	Login Attempt Limit with While Loop
# Give user 3 attempts to enter correct password. Lock account after 3 wrong attempts.
# 🔹 [while, break, if]

# username='swathi'
# password='12345'
# max_attempts=3
# attempts=0
# while attempts<max_attempts:
#     user=input('Enter username: ')
#     pwd=input('Enter password: ')
#     if user == username and pwd == password:
#         print('Login successful')
#         break
#     else:
#         attempts += 1
#         print(f'Incorrect credentials.Attempts left: {max_attempts-attempts}')
# if attempts == max_attempts:
#     print('too many attempts failed,login denied')
# 4.	Recursive Dictionary Flattener (Full)
# Input deeply nested dictionary and flatten all keys.
# Example:

#  	🔹 [recursion, nested dict, loops]
d2={"a": {"b": {"c": 1}}, "x": 2}
fla={}
#  	🔹 [recursion, nested dict, loops]
for key,value in d2.items():
    if isinstance(value,dict):
        for k,j in value.items():
            if isinstance(j,dict):
                for l,m in j.items():
                   fla[f'{key}/{k}/{l}']=m
            else:
                fla[f'{key}/{k}']=j
    else:
        fla[f'{key}']=value
print(fla)

# 5.	Pascal Triangle Full Pattern
# Input = 5
# Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
#  	🔹 [loops, nested logic, combination math]

# n=int(input('enter the number of rows: '))
# for i in range(n):
#     print(' '* (n-i), end="")
#     num=1
#     for j in range(i +1):
#         print(num, end=' ')
#         num=num*(i-j) // (j +1)
#     print()
# ________________________________________
# 🧠 Set 5: Balanced Assessment
# 1.	Area Calculator for Circle or Square
# Input shape type (circle or square) and compute area.
# 🔹 [if-elif-else, float, operators]

# shape=input('Enter shape(square/circle):').strip().lower()
# if shape == 'square':
#     side=float(input('enter the side length: '))
#     area= side * side
#     print(f'Area of square: {area}')
# elif shape =='circle':
#     radius=float(input('enter the radius: '))
#     pi= 3.14
#     area= pi * radius * radius
#     print(f'Area of circle: {area}')
# else:
#     print('Invalid Shape')

# 2.	List Intersection Without `\    Input two lists, print common elements without usingset`.
# 🔹 [list, loops, conditionals]

# list1=[int(x) for x in input('enter first list elements(space-separated):').split()]
# list2=[int(x) for x in input('enter second list elements(space-separated):').split()]
# common=[]
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print('Common elements:',common)


# 3.	Temperature Alert System (Nested If)
# Input temperature and humidity:
# o	If temp > 40:
# 	If humidity > 60 → “Hot & Humid”
# 	Else → “Only Hot”
# o	Else → “Normal”
# 🔹 [nested if, bool]
# temperature=float(input('enter the temperature in celsius'))
# humidity=float(input('enter the current humidity in %'))
# if temperature<0:
#     temp_alert='Freezing temperature'
# elif temperature<= 35:
#     temp_alert='Normal temperature'
# elif temperature<= 45:
#     temp_alert='High temperature!'
# else:
#     temp_alert='Exteremly high!'
# if humidity < 30:
#     hum_alert='Low humidity,air is dry'
# elif humidity <= 60:
#     hum_alert='Humidity is normal'
# else:
#     hum_alert='High humidity!'
# print('\n----Alert Report----')
# print(f'Temperature: {temperature}c->{temp_alert}')
# print(f'Humidity:{humidity}% ->{hum_alert}')


# 4.	Flatten and Sort All Values from Dict
# Input:
#  	{'a': {'x': 5, 'y': 3}, 'b': 1, 'c': {'z': 2}}
#  	Output: List of all values sorted: [1, 2, 3, 5]
# 🔹 [dict, nested dicts, data extraction]
d1 = {'a': {'x': 5, 'y': 3}, 'b': 1, 'c': {'z': 2}}
fl= {}
for key, value in d1.items():
    if isinstance(value, dict):
        for k, j in value.items():
            fl[f'{key}/{k}'] = j
    else:
        fl[f'{key}'] = value
print(fl)



# 5.	Double-sided Arrow Pattern
# Input: 5
# Output:
#  	    1
#    2 1 2
#   3 2 1 2 3
#  4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5
#  	🔹 [nested loops, number symmetry, conditionals]
# n=int(input('enter the number of rows: '))
# for i in range(1, n + 1):
#     print(' '* (n-i), end='')
#     for j in range(1,i + 1):
#         print(j, end=' ')
#     for j in range(i - 1,0, -1):
#         print(j,end=' ')
#     print()
