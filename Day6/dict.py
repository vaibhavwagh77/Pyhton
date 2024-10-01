dict={'a':1,'b':2,'c':3,'d':4}
print(dict)

print(dict['c'])
print(dict.get('c'))

dict={1:'a',2:'b',3:'c',4:'d'}

print(dict)


#value that a dist. can take 

#mutable
#powerful and felxiable'
# storing and mangeing the complex data
#Doictionries are indexed by uniques keys
my_dict = {
    "integer_value":2,
    "string_value":"this is string",
    "tuple_value": (1,2,3),
    "list_value":(1111,222,333,455,6566)

}



print(my_dict)
print(my_dict['list_value'])
print(my_dict.get('tuple_value'))

# dic_value=my_dict.pop(1)
# print(dic_value)
# print(dic_value)

#delete in the dic for the element
"""del my_dict[3]
print(my_dict)"""



#CHECKING for keys

# if 2 in dict:
#     print("key\'2\' is present")
# else:
#     print("key\'2\' is not present")

#itrate over the dictionires

dic={'a':1, 'b':2, 'c':3}
for key in dic:
    print(key)

# Iterating over key-value pairs

for key, value in dic.items():
    print(f"{key}:{value}")

#Merging the dictonaries
dict1={'a':1, 'b':2, 'c':3,}
dict2={'d':4, 'e':5}

dict1.update(dict2)
print(dict2)

#how to make the dic the empty dic

print(dict1)
dict1.clear()
print(dict1)