# Create an empty dictionary called bird

bird={}
# Add name, color, breed, legs, age to the bird dictionary

bird.update({'name':'Parrot','colour':'Green','breed':'abc','legs':2,'age':2})
print(bird)
# Create a student dictionary and add first_name, last_name, gender, age, marital_status,
# skills, country, city and address as keys for the dictionary

student_dic={'First_name':'Rama','Last_name':'Krishna','Gender':'Male','Age':23,'Maritial_status':'Single',
         'Skills':'Python','Country':'India','City':'Bangalore','Address':'abcdefgh'}
print(student_dic)

# Get the length of the student dictionary
print(len(student_dic))
# Get the value of skills and check the data type, it should be a list

print(type(student_dic.get('Skills')))
# Modify the skills values by adding one or two skills

student_dic['Skills']=['Python','Java','Cpp']
print(type(student_dic.get('Skills')))
# Get the dictionary keys as a list

print(list(student_dic.keys()))

# Get the dictionary values as a list

print(student_dic.values())
# Change the dictionary to a list of tuples using items() method

print(list(student_dic.items()))
# Delete one of the items in the dictionary

print(student_dic.pop('Country'))
print(student_dic)

# Delete one of the dictionaries

del(bird)
print(bird)