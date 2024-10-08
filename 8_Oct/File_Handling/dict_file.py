def writ_dict_to_file(filename, my_dict: dict):
    details={}
    with open("filename", 'w') as f:  
        for key, value in details.items():  
            f.write('%s:%s\n' % (key, value))


my_dict={'name':'vaibhav','Roll No':'20','Science':'40','Maths':'50'}
writ_dict_to_file('dict.txt',my_dict)















    '''def write_list_to_file(filename: str, my_lsit: list):
    with open(filename, 'a')as file:
        for item in my_list:
            file.write(f"{item}\n")


my_list=['apple', 'banana','cherry']
write_list_to_file('example.txt', my_list)'''