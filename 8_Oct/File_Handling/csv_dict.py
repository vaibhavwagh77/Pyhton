# sample dictionry data (single record)
data={'Name':'vaibhav','age':23,'city':'nashik'}
filename='student.csv'
#writing to a csv file
with open(filename, mode='w', newline='') as file:
    #get the keys of the dictionry as filename for the header
    filednames=data.keys()
    