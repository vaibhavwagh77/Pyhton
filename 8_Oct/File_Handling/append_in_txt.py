def write_list_to_file(filename: str, my_lsit: list):
    with open(filename, 'a')as file:
        for item in my_list:
            file.write(f"{item}\n")


my_list=['apple', 'banana','cherry']
write_list_to_file('example.txt', my_list)