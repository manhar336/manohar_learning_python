#!/usr/bin/python
name = "Guido Van Rossum"
name1="version96"
name2 = "      test      "
name3 = "$$$$$$test1,test2,test3$$$$$$"
print("capatalize method and converts first letter convert into capital :",name.capitalize())
print("center method:",name.center(22,'#'))
print("center method without giving any fill with chars then print spaces",name.center(22))
print("count method with giving some char and giving starting and ending values",name.count('o',0,16))
print("count method2 with giving only starting index:",name.count('o',0))
print("count method3 with only word",name.count('Guido'))
print("")
print("starts with method in strings:",name.startswith('Guido'))
print("starts with method2 in strings:",name.startswith('guido',0))
print("ends with method1 in strings:",name.endswith('Rossum'))
print("")
print("find method in string:",name.find('Rossum'))   #find method  will give index value
print("index method in strings:",name.index('Rossum')) #Index method also give inddex value
print("")
print("Is alpha numeric method:",name1.isalnum())  #alpha numerc method considered number and alpha along with spaces as well
print("Is alpha method:",name1.isalpha())
print("Is lower case method:",name1.islower())
print("Is upper case method:",name.isupper())
print("swap case method:",name.swapcase())   #it will swap lower to upper case and vice versa
print("is space method:",name.isspace())
print("is title method",name.istitle())   #pass because starts with every word with capital letter
print("strip method:",name2.strip())
print("strip method1:",name3.strip('$'),type(name3))   # it will remove special chars on left and right hand sides
print("left hand strip method:",name2.lstrip())
print("min method in strings:",min(name1))
print("max method in strings:",max(name1))
print("replace method in string:",name.replace('G','M'))
print("split method in string",name.split())
print("split method1 in string",name3.split("$"))
print("split method2 in string",name3.splitlines("$"))
print("split lines",name3.splitlines())