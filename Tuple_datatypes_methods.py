atuple = ("test","1","test2","test3")
print(atuple,type(atuple),id(atuple),tuple(enumerate(atuple)))
print("printing tuple in different options:",atuple[0:2],atuple[0::2],type(atuple),tuple(enumerate(atuple)))
print("printing tuple using string parameters:%s%s%s%s"%(atuple))
list1 = [1,2,3,4]
tup1= tuple(list1)
print(tup1,type(tup1))
tup2 , tup3 = ("1","2","3","4") , ("5","6","7")
print(tup2,tup3,tuple(enumerate(tup2)),tuple(enumerate(tup3)))
print (tuple('abc'))
print(tuple([1, 2, 3, 4, 5]))
print (tuple((1, 2, 3, 4, 5)))
print(tuple({1: 2, 3: 4}))

#iterate through the items and print the values
for x in atuple:
    #print(x)
    print(x)

#check if item exists or not
if "test" in atuple:
    print("value exist")
else:
    print("value does not exist")

#min and max method
print("min method in tuple:",min(atuple))
print("max method in tuple:",max(atuple))

#concatenation method
tup4 = (1,2,3,4)
tup5 = 'name1','name2','name3'
tupleconcatenation = tup4 + tup5
print(tupleconcatenation,type(tupleconcatenation),tuple(enumerate(tupleconcatenation)))

