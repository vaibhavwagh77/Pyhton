list=[]  
def add_music(song):
    list.append(song)
    print(f"{song} has been added to end playlist") 
    
def remove_music(song):
    
    if song in list:
        list.remove(song)
        print(f"{song} has been removed")
    else:
        print("The song is not there in the list")
    
def view_all():
    if list:
        print(" The list is ")
        for index, song in enumerate(list,1):
            print(f"{index}.{song}")
        else:
            print("The list is empty")
            
def slice(start,end):
    return list[start:end]



add_music("song1")
add_music("song2")
view_all() 
print("Slice list:",slice(0,2))    
remove_music("song1")
view_all()
print("Slice list:",slice(0,1))        

