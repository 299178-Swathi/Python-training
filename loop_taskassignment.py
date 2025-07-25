
for i in range(11):
   print(i)

i=0
while i<=10:
   print(i)
   i +=1

for i in range(10,0,-1):
   print(i)

i=10
while i>=0:
   print(i)
   i -=1

for i in range(8):
  print('# # # # # # # #')

for i in range(11):
  print(f"{i}x{i}={i*i}")

l=['Python','Numpy','Pandas','Scikit', 'Pytorch']
for i in l:
   print(i)

for i in range(2,100,2):
   print(i)

for i in range(1,100,2):
   print(i)

total=0
for i in range(101):
   total += i
print('sum of numbers 0 to 100 is:',total)

total=0
for i in range(2,100,2):
   total += i
print('sum of all even numbers between 0 to 100 is:',total)

total=0
for i in range(1,100,2):
   total += i
print('sum of all the odd numbers between 0 to 100 is:',total)


total_even=0
total_odd=0
for i in range(101):
  if i%2==0:
  total_even += i
  else:
  total_odd += i
print('sum of all the even numbers between 0 to 100 is:',total_even)
print('sum of all odd numbers between 0 to 100 is:',total_odd)

row=7
for i in range(1,row+1):
    for j in range(row-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('#', end='')
    print()

