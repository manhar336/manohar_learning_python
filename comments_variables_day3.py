#!/usr/bin/python means where python installed
#Single line comments: '',#,""
#Multi line comments:''' ''',""" """

#Creating variables in python
firstname = 'Guido'
MiddleName = "Van"
Lastname = """Rossum"""
Invention = '''Python'''
YEAR = 1980

#calling or accessing variables in python
print(firstname)
print(MiddleName)
print(Lastname)
print(Invention)
print(YEAR)
print("First Name:\t",firstname,"Middle Name:\t",MiddleName,"Lastname:\t",Lastname,"""Invention:\t""",Invention,"Year:\t",YEAR)
print("Firstname:%s"%(firstname),"Year:%i"%(YEAR))

print(firstname,type(firstname),id(firstname))