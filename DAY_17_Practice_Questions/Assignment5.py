# def translate(string):
#     vowels = 'aeiouAEIOU' #vowels
#     translate=''
#     for char in string:
#         if char in vowels:
#             translate+='abc'
#         else:
#             translate+=char
#     return translate
# input_string = "This is fun."
# output_string = translate(input_string)
# print(output_string) 


def translate(string):
    vowel = "aeiouAEIOU"
    translate= ""
    for char in string:
        if char in vowel:
            translate+="abc"
        else:
            translate += char
    return translate
input="list"
output=translate(input)
print(output)
