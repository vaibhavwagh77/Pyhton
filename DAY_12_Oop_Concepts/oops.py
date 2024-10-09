class clsPhonebook:
    strName=""
    strPhone=""
    strAddres = ""
    
    def __init__(self,name,clsPhonebook,add):
    #attributeds of theclass
        self.strName= name
        self.strPhone=clsPhonebook
        self.strAddres= add
    
    def setValue(self,name,clsPhonebook,add):
        self.strName= name
        self.strPhone=clsPhonebook
        self.strAddres= add
    
    def display_phonebook(self):
        print("Name: ",self.strName)
        print("Phone number: ",self.strPhone)
        print("Address: ",self.strAddres )
    
if __name__=="__main__":
    objPhonebook1=clsPhonebook("Vaibhav","93796755","New-Delhi")
    objPhonebook2=clsPhonebook("Wagh","93796777","Nashik")
    objPhonebook1.display_phonebook()
    objPhonebook2.display_phonebook()
    
    
lstObjList=[]
lstObjList.append(objPhonebook1)
lstObjList.append(objPhonebook2)
for item in lstObjList:
    item.display_phonebook()