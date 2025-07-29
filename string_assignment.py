#     Conceptual Questions
# Explain the difference between immutable and mutable types in Python. How does this apply to strings?
#
#In Python mutable and immutable data refers to whether the value of the object can be changed after created
#Mutable Datatype
#Objects who's content can be changed in place without changing their memory address(Ex:[List],{dictionary},{set})
#Operations like adding,removing or updating elements modify the same object

#Immutable Datatypes
#Objects who's content cannot be changed after creation.Any change creates a new object with different identity.
#(Ex:(tuple),('string'),int)
#how it applies to string
#String is a immutable data,once it is created it cannot be changed in place.Operation like concatenation or
#replace creates the new string with new address.

# Describe the role of escape characters in Python strings. Give examples.
#In string,an escape character is used to represent characters that cannot be typed directly or have a special
#meaning in the string literal
#The escape character is the backlash(\).When python sees the backlash inside the string it treats the next
#character as having a special interpretation.

# Coding Questions
# Write a Python program that takes a string and removes all vowels.

str1=('I Love Python,I like to work on python')
vowels='aeiouAEIOU'
result=''
for char in str1:
    if char not in vowels:
        result += char
print('Orginal String:',str1)
print('String without vowels:',result)
# Given a string, write a program to count the frequency of each character.

freq={}
for char in str1:
    freq[char]=freq.get(char,0) + 1
print('Character frequency:')
for key,value in freq.items():
    print(f'{key}:{value}')

# Write a Python program to check if two given strings are anagrams of each other
l1=input('enter the first string')
l2=input('enter the second string')
l1=l1.upper()
l2=l2.upper()
if sorted(l1)==sorted(l2):
    print('strings are anagram of each other')
else:
    print('Not anagram')

# Write code to reverse the order of words in a sentence, without using built-in reverse functions

str2='python is a high level programming language'
words=str2.split()
rev_words=[]
for i in range(len(words)-1,-1,-1):
    rev_words.append(words[i])
rev_str2=' '.join(rev_words)
print('Original String:',str2)
print('Reversed string:',rev_str2)

# Write a Python program to find the longest substring without repeating characters.
# Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
s='i am working at ust'
rev=''
for i in s:
    rev = i + rev
if s==rev:
    print('Yes')
else:
    print('No')
# Write code to convert a string so that the first letter of each word is capitalized (like title case),
# without using .with out using Title()
s1='hello world welcome to python'
wrd=s1.split()
for j in range(len(wrd)):
    wrd[j] =wrd[j][0].upper() + wrd[j][1:]
re=' '.join(wrd)
print(re)
