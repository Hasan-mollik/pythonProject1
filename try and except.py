
try:
    print("give me a output 1 line")
except:
    print(x)

print("give me a car")
print("give me a money")
print("give me a function")

#or
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#or

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
