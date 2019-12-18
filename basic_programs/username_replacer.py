'''
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P​ -> Take User Name as Input. ​ Ensure UserName has min 3 char
b. Logic​ -> Replace <<UserName>> with the proper name
c. O/P​ -> Print the String with User Name
'''

from utils import Util

name = str(input("Enter a Username: "))

name_object = Util()
new_string = name_object.get_username(name)
print(new_string)
