#list comprehension:
num=[1,3,5,7,9]
#for x in num:
#print(x*2)
Double= [x*2 for x in num]
print(Double)

#sort list
num=[9,5,7,3,1]
num.sort()
print(num)
#word sort
word=['d','f','s','a','e']
word.sort()
print(word)

#reverse list
num=[1,3,5,7,9]
num.sort(reverse=True)
print(num)

#copy list
num=[1,2,3,5,7,8,9]

num2=num.copy()
num.copy()
print(num)
print(num2)

#join list
num1=[1,3,5]
num2=[2,4,6]
#num3=num1+num2
#print(num3)
num1.extend(num2)
print(num1)

#while loop
i = 1
while i < 6:
  #print(i)
  i+= 1

#breakstatement
i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
#continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else condition
i = 0
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#break method

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#continue method
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

