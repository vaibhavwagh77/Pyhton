single_quotes='vaibhav'
double_quotes="vaibhav Wagh"
triple_quotes='''vaibhav'''

print(type(single_quotes))
print(double_quotes)
print(triple_quotes)


escape_sequence='hi weather is \'good\'!\n\t have a nice day!!'
print(escape_sequence)


#concatenation

str1="the fox is not nice animal "
str2="but it is clever"

result=str1+str2
print(result)




length = len(result)
print(length)

str1="abcdefghijklmnopoqrstuvwxyz" + "  ."
print(str1)
print(len(str1))


stripped_string= str1.strip()
print(stripped_string)

print(len(stripped_string))


postion=result.find("fox")
new_string= result.replace("fox","Fox")
print(postion)
print(new_string)


str1="vaibhav"
str2="vaibha2"
resut = str1==str2

print(resut)