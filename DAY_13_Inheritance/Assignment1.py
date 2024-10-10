#Calculate the area of shape
#base class (parent class/super class)
class shape_name:
    
    def __init__(self):
        
        self.shape_name=""
        
    def user_input(self):
        self.shape_name=input("Enter the shape you want: ")
        
    def area(self):
        if self.shape_name=="circle":
            radius=float(input("Enter the raidus: "))
            self.area=radius**2*3.14
        elif self.shape_name=="square":
            side1=int(input("Enter the lenght of one side: "))
            self.area=side1**2
                        
    def display(self):
        if self.area > 0:
            print(f"The area of {self.shape_name} is {self.area}")
        else:
            print(f"{self.shape_name} is not a proper shape")
    
shapeobj=shape_name()
shapeobj.user_input()
shapeobj.area()
shapeobj.display()    
    
