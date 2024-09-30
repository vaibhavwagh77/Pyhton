#the output of the example is 
'''()
(1,)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
10
20
30
(1, 2, 3, 4, 5, 6, 7, 8)
(1, 2, 3, 2, 2, 2)
True
True
5
2
[1, 2, 3, 4, 5, 6, 7, 9, 87]
(1, 2, 3, 4, 5, 6, 7, 9, 87)'''

a1=()#empty tuple
a2=(1,)#tuple with only one element with comma
a3=(1,2,3,4,5,6,7,8,9)#tuple wwwith more than one element

print(a1)
print(a2)
print(a3)


#assign the the aplhabate a value in the tuple
my_tuple=(10,20,30)

a,b,c=my_tuple
print(a)
print(b)
print(c)


#concentation in this case the original tuple is not changed but we have to make a new 
#tuple

tupel1=(1,2,3,4)
tuple2=(5,6,7,8)

concentation_tuple=tupel1+tuple2
print(concentation_tuple)

#lenth of the tuple
tuple_len=(1,2,3,4,5,6,7,8,9)
length=len(tuple_len)

#repeat the items from table as much they want that is 3 in this case
t1=(1,2,3,2,2,2)
repeat=t1*3
print(t1)


#checking the membership
my_tup=(1,2,3)
its_present=2 in my_tup
print(its_present)
its_present=2 in my_tup
print(its_present)

#counting occurence in the tuple
tup1=(1,2,2,2,2,2,3,4,5,6,7,8,9)
count_of_twos= tup1.count(2)
print(count_of_twos)

#finding the index in the tuple

my_t1=(1,2,3,4,5,6,7,8,9)
ondex_of_three=my_t1.index(3)
print(ondex_of_three)

#sorting the tuple in ascending order
myt2=(1,2,3,4,5,6,7,87,9)
myt2_list=sorted(myt2)
print(myt2_list)#in the form of list it will give the converting tuple in the list

#Converting the list in the tuple

myt2= tuple(myt2_list)
print(myt2)

#converting the tuple to the list





