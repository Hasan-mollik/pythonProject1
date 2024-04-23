class baba:
    car="toyoto"
    taka="1 crore"
    home="10th floor"

class baba2:
    smartphone="Iphone"
    Ac="walton"
    microphone="fifine"


class baba3:
    webcam="Iphone"
    laptop="walton"
    camera="fifine"

    brokenphone=""
    brokenhome=""

#k = kaka()
#print(k.camera)
#print(k.laptop)


#multilevel inheritance

class baba:
    car = "toyoto"
    taka = "1 crore"
    home = "10th floor"


class son1(baba):
    smartphone = "Iphone"
    Ac = "walton"
    microphone = "fifine"

class son2(son1):
    webcam="Iphone"
    laptop="walton"
    camera="fifine"

class son3(son2):
    brokenphone=""
    brokenhome=""

k=son3()
print(k.home)

#iterator
mytuple = ("apple", "banana", "cherry")
x = iter(mytuple)

print(next(x))
print(next(x))
print(next(x))

#scope
def myfunc():
  x = 300
  print(x)

myfunc()

#global scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)
#or
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)
