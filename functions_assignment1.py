# 2.12. 💻 Exercises ➞ Functions
# 2.12.1. Exercises ➞ Level 1
# Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
# Write a function that calculates area_of_circle and perimeter_of_circle.
def area_perimeter(radius):
    pie=3.14
    area=pie*radius*radius
    perimeter=2*pie*radius
    return area,perimeter
n=float(input('enter the radius '))
area,perimeter=area_perimeter(n)
print(f'Area of circle:',{area})
print(f'Perimeter of circle:',{perimeter})

# Write a function called add_all_nums which takes arbitrary number of arguments and
# sums all the arguments. Check if all the list items are number types. If not do give a reasonable
# feedback.

def add_all_nums(*args):
    if all(isinstance(arg,(int,float))
for arg in args):
        return sum(args)
    else:
        return (f'Error: All inputs must be numbers int or float')
print(add_all_nums(34,45,76,89,65,67))
print(add_all_nums(56,67,78,56))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function
# which converts °C to °F, convert_celsius_2_fahrenheit.

def celsius_fahren(celsius):
    return(celsius*9/5)+32
print(celsius_fahren(103))

# Write a function called check_season, it takes a month parameter and returns the season: Autumn,
# Winter, Spring or Summer.

def check_season(month):
    if month in('december','january','february'):
        return 'Winter'
    elif month in('march','april','may'):
        return 'Summer'
    elif month in('june','july','august'):
        return 'Autumn'
    elif month in('september','october','november'):
        return 'Spring'
    else:
        return 'Error,month name is invalid'
print(check_season('hello'))

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(x1,x2,y1,y2):
    return(y2-y1)/(x2-x1)
print(calculate_slope(2,5,6,9))

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates
# solution set of a quadratic equation, solve_quadratic_eqn.
# def quadratic_equation()

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of
# the list.
def print_list(*args):
    for arg in args:
        return list(args)
    else:
        return 'not a list'
print(print_list(11,22,33,44,55,66,77))

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of
# the array (use loops).
def reverse_list(array):
    reverse_array=[]
    for arr in range(len(array)-1,-1,-1):
        reverse_array.append(array[arr])
        return reverse_array
    else:
        return 'Not a array'
num=[11,22,33,44,55,66]
print(reverse_list(num))



# print(reverse_list([1, 2, 3, 4, 5])) #[5, 4, 3, 2, 1] print(reverse_list1(["A", "B", "C"]))
# #["C", "B", "A"] ```
def reverse_list(list1,list2):
    return list1[::-1],list2[::-1]
a=[1,2,3,4,5]
b=['A','B','C']
print(reverse_list(a,b))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a
# capitalized list of items
def capitalize_list_items(items):
    for i in range(len(items)):
         items[i]=items[i].capitalize()

words=['raghavendra','hanumantha','narasimha']
capitalize_list_items(words)
print(words)


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with
# the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(add_item(food_staff, 'Fungi'))
# #['Potato', 'Tomato', 'Mango', 'Milk', 'Fungi'] numbers = [2, 3, 7, 9] print(add_item(numbers, 5))
# #[2, 3, 7, 9, 5] ```

def add_item(mylist,item):
    mylist.append(item)
    return mylist
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers=[2,3,7,9]
print(add_item(food_staff,'Fungi'))
print(add_item(numbers,5))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'] print(remove_item(food_staff, 'Mango')) # ['Potato', 'Tomato', 'Milk'] numbers = [2, 3, 7, 9] print(remove_item(numbers, 3)) # [2, 7, 9] ```
# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in
# that range.
def sum_of_numbers(start,end):
    total=0
    for i in range(start,end +1):
        total += i
    return total

print(sum_of_numbers(6,15))

# print(sum_of_numbers(5)) # 15 print(sum_all_numbers(10)) # 55 print(sum_all_numbers(100)) # 5050 ```

def sum_of_numbers(a):
    total=0
    for i in range(a):
        total = total+i
    return total
print(sum_of_numbers(6))
print(sum_of_numbers(11))
print(sum_of_numbers(101))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in
# that range.
def sum_of_odds(numbs):
    total=0
    for numb in range(numbs):
        if numb%2!=0:
            total += numb
    return total

print(sum_of_odds(15))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in
# that - range.
def sum_of_even(numbs):
    total=0
    for numb in range(numbs):
        if numb%2==0:
            total += numb
    return total

print(sum_of_even(15))