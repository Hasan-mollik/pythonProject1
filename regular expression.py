import re

txt = "The rain in Spain"
x = re.findall("[a-m]",txt)
print(x)

#0r
import re
 
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")

#split function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#or
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#sub function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
#0r
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
