#Q1)Create list called "even", store all the even numbers, in the range of 1 to 20

even=[]
for num in range(1,21):
    if num%2==0:
        even.append(num)
print(even)

#Q2) Create list called "odd", store all the odd numbers, int the range of 1,20

odd=[]
for num in range(1,21):
    if num%2!=0:
        odd.append(num)
print(odd)

#Q3) Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.

numbers=even+odd
numbers.sort()
print(numbers)

#Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks]

students=[['Swathi',24,89.6],['Nishank',21,92.4],['Nishvika',19,91.2],['Shashi',20,76.2],['Murthy',10,78.7]]
print(students)

#Write a Python program to find the second largest number in a list

l1=[276,456,289,678,278]
l1.sort()
seclar=l1[-2]
print(l1)
print(seclar)

#Q6) WAP to print unique element from list.     ex... nums = [4,3,5,6,3,4,6]      (o/p:- 5 is unique from list)

nums = [4,3,5,6,3,4,6]
unique_num=[num for num in nums
    if nums.count(num)==1]
print(unique_num)

#Q7) Given a tuple of numbers, find the max and min elements.
#  ex.. tup = (11,26,45,23,15,18)

tup=(11,26,45,23,15,18)
tup1=list(tup)
tup1.sort()
print(tup1[0])
print(tup1[5])

#Q8) Retrieve the 'G' from following list using positive indexing

L1 = [1, 2, 'hi', (21, 78, [-2, -4, ('Bahubali', 'KGF', 'RRR')])]
print(L1[3][2][2][1][1])

#Q9) WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

#Q10) WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
s2 = 'Hello I am going to Bengaluru How are you doing?'
reverse_bangalore=s2[-20:-29:-1]
print(reverse_bangalore)






