def reverse_string(s):
    if len(s) == 0 or len(s) ==1:
        return s
    else:
        return reverse_string(s[1:])+s[0]

input_string=input("Enter the string you want to reverse: ")
reversed=reverse_string(input_string)
print(reversed)