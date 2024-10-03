def sum_of_list(lst):
    return sum(lst)

number= [1,2,3,4,5,6,7,8,9]
result=sum_of_list(number)
print(result)


def count_frequency(lst):
    count=0
    
    for i in lst:
        
        count=count*i
        i=i+1
    return(count)
    
num=[1,2,3,4,5,6,7,8,9,]
result1=count_frequency(num)
print(result1)


def occurnance(lst):
    dic={}
    for i in lst:
        if i in dic :
            dic[i]+=1
        else:
            dic[i]=1
    return dic
    
lsit=[1,2,1,2,3,4,5]
result2=occurnance(lsit)
print(result2)

def sum_product(lst):
    count=0
    count1=0
    for i in lst:
        
        count=count*i
        count1=count1+i    
        
        i=i+1
    
    # count1=0
    # for i in lst:
    #     count1=count1+i    
    #     i=i+1
    return (count1,count)
n1=[1,2,3,4,5,6,7,8,9]

res=sum_product(n1)
print(res)