Myset={1,"false","string",}
print(Myset)
#print(type(Myset))
#seen leen
set={1,2,3,4,5,6,}
print(len(set))

#acess set item
set={1,3,5,7,9}
#for x in set:
    #print(x)
5 in set
print(5 in set)

#add set item
Myset={"rasel","mehedi","najmul","hasan"}
Myset.add("taijul")
print(Myset)

#set update method
set2={1,3,5,7,}
set3={2,4,6,8}
set2.update(set3)
print(set2)

#adding update list
set={1,2,3,4}
list=[5,6,7,8]
set.update(list)
print(set)

#remove set item
myset={1,3,5,7,9}
#myset.remove(7)
#print(myset)

#discard method
myset.discard(9)
print(myset)

#discard method
myset.discard(8)
print(myset)

#pop method
set3={'hasan','mehedi','rasel'}
#set3.pop()
#print(set3)

#clear method
set3.clear()
print(set3)

#set loop
fruits={"orange","banana","mango"}
for x in fruits:
    print(x)

#join set
set1={1,3,5}
set2={2,4,6}
#set1.union(set2)
#print(set1)

#update method
set2.update(set1)
print(set2)

#set intersection

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)
