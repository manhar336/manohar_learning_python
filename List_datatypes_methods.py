a_list = [1,2,'aws','devops','python',("test1","test2","test3")]
acoollist = ["superman","spiderman","man",10,20,"spiderman"]
onemorelist = [10,20,30,40,50,20,20]
morelist = [(10,20,30,40),(10,20,30,40)]
a=(10,20,30,40)

print(a_list,type(a_list),list(enumerate(a_list)))
print(acoollist.index("superman"))
print(acoollist.index(10,0))
acoollist.reverse()
print("reverse method in a list:",acoollist)
print("count method1 in a list",acoollist.count('aws'))
print("count method2 in a list",a_list.count('aws'))
print("count method3 in a list",morelist.count(a))
acoollist.append('superhero')
print("append method in a list:",acoollist,len(acoollist),list(enumerate(acoollist)))
acoollist.extend(onemorelist)
print("extend method in a list:",acoollist)
morelist.extend(a)
print("extend method in a list:",morelist)
morelist.insert(1,('name1',"name2","name3"))
print("insert method in a list",morelist)
print("delete one index element by using pop memthod:",acoollist.pop())
a_list.remove('aws')
print("remove one element using remove method",a_list)
onemorelist.sort()
print("sort method in a list",onemorelist)
print("minimum value in a list:",min(onemorelist), "max value in a list:",max(onemorelist))
if 20 in a_list:
    a_list.count(20)
elif "aws1" in a_list:
    a_list.insert(2,'aws2')
else:
    a_list.extend(onemorelist)
    print("Membership operators",a_list)
#item assignment
acoollist[1] = 'anshul'
print(acoollist)
print("copying",a_list.copy())

name =[]
name.extend([1,2,3,4])
print(name)

