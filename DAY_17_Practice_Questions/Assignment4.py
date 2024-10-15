students = {'Mayura': 89, 'Pravin': 92, 'ketki': 95, 'Chinmay': 99}
print("Original students dictionary:", students)

def student_operations(student_dict):
    total_students = len(student_dict)
    print(f"Total number of students: {total_students}")
    
    if 'Pravin' in student_dict:
        student_dict['Pravin'] = 85
        print("Updated marks of Pravin to 85.")
        
    if 'ketki' in student_dict:
        del student_dict['ketki']
        print("Removed Ketki and her marks.")
        
    sorted_students = dict(sorted(student_dict.items()))
    print("The sorted dictionary is:")
    for student, marks in sorted_students.items():
        print(f"{student}: {marks}")

student_operations(students)
