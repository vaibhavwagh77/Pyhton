people={'Vinay':'Blue','Vaibhav':'Pink', 'Siddhart':'Black', 'Suraj':'Green(maqsad)'}

total=len(people)
print(f"The total students are {total}")

#change ram colour

people['Vaibhav']='white'

#remove

people.pop('Suraj')

#sort

sorted_people=dict(sorted(people.items()))

print(sorted_people)
