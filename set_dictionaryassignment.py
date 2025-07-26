# Q1) Create a dictionary named student_info with the following keys:student_name, age, roll_no, class, section, percentage, college_name.

#a) Print all the keys and values from the dictionary.

Student_info={'student_name':'Sameera','Age':21,'Rollno':15,'Class':'Accounts','Section':'C','College_name':'CMR'}
print(Student_info)

#b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.

Student_info['email']='sameera21@mail.com'
print(Student_info)

#c) Delete the section key from the dictionary.

Student_info.pop('Section')
print(Student_info)

#d) Use a loop to print all key-value pairs in the dictionary in the format:# Key --> Value

for keys,values in Student_info.items():
    print(f'{keys}:{values}')

#e) Check if the key 'college_name' exists in the dictionary or not

print('College_name' in Student_info)

python_students = {"Alice","Bob","Charlie","David"}
java_students = {"Bob","Eve","Frank","David"}
cpp_students = {"Charlie","George","Eve","Henry"}
# Find students who are enrolled in all three courses.
common_students=python_students.intersection(java_students,cpp_students)
print(common_students)

# Find students who are enrolled in only Python course.
only_python=python_students-(java_students|cpp_students)
print('students who enrolled only in python:',only_python)

# Find students who are enrolled in both Python and Java.
python_java=python_students&java_students
print('students enrolled both in python and java:',python_java)

# Find students who are enrolled in either Python or Java but not both.

not_both=python_students.symmetric_difference(java_students)
print('students not in both courses:',not_both)


# Find the list of all unique students enrolled in any course.

unique_students=python_students|java_students|cpp_students
print('unique students enrolled in any courses:',unique_students)

# Find students who are in Java or C++, but not in Python.

not_python=(java_students|cpp_students)-python_students
print('students not in python:',not_python)

# Check if all Python students are also Java students.

also_java=python_students.issubset(java_students)
print(also_java)

# Add a new student "Jones" to the Python set.
python_students.add('Jones')
print(python_students)

# Remove "Frank" from the Java set.
java_students.discard('Frank')
print(java_students)


# Clear the cpp_students set.

cpp_students.clear()
print(cpp_students)


