a_cooldict = {"firstname":"manohar","lastname":"Dharmala","age":36}
a_coollist = [1,2,3,4]
a_tuplist = ("name1","name2","name3")
initial = {}
initial["wife"] = "chinta"   #item assignment
initial["mine"] = "Dharmala"
print(initial,type(initial),dict(enumerate(initial)),len(initial),id(initial))
print("printing only keys in dict:",initial.keys())
print("printing only values in dict:",initial.values())   # it will give all values in dict
print("printing values using get method:",initial.get('wife'))  #it will give specific value
print("printing values using type2 get method:",initial.get("son","dharmala"))
print(initial)
print("printing values using set default method:",initial.setdefault("son","chinta")) #it will change value for particular key
print("printing one more value using set default method:",initial.setdefault("amma","dharmala")) #we can assign new keys and values
print("printing keys and values in item method:",initial.items()) #it will give keys and values in list method
print("changing list into dictionary using from keys method:",dict.fromkeys(a_coollist))  #values print as none
print("giving values for updated using get from method",dict.fromkeys(a_coollist,'python'))  #values print as python for all keys
a_cooldict.update(initial)
print("joining 2 dictionaries:",a_cooldict)
del initial["son"]  # it will delete only one key
print(initial)
del initial
#print(initial)
a_cooldict1=a_cooldict.copy()  # it will just copy original dictionary
print(a_cooldict)
print("removing one value  using pop method:",a_cooldict1.pop('firstname'))

for x,y in a_cooldict.items():
    print("keys of a_cooldict:",type(x))
    print("values of a cooldict:",type(y))

if "firstname" in a_cooldict:
    print(a_cooldict.keys())

