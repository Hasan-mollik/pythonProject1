#update tuple
x = ("apple", "banana", "cherry")
y=list(x)
y.append("orange")

z=tuple(y)
print(z)

#unpack tuple
fruits=("apple", "banana", "cherry","carrot")

(a,*b)=fruits
#print(b)
print(b)
