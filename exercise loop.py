list=['mango','orange','apple','jackfruit']
for x in list:
    #print(x)

#use range and len()
    for x in range(len(list)):
        print(x)

#while loop
y=0
while y<len(list):
    print(list[y])

    y = y+1

#list comprehension
num=[1,3,5,7,9]
for x in num:
    print(x*2)
d=[x*2 for x in num]
print(d)

#sort list
num=[1,8,6,4,3]
num.sort()
print(num)

eng=['a','d','c','g']
eng.sort()
print(eng)

#reverse list
num=[1,2,7,6,8]
num.sort(reverse=True)
print(num)



