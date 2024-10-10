class parent_A:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def math_operation(self):
        super().math_operation()
        result=self.num1+self.num2
        print(result)
        
class child_B(parent_A):
    def math_operation(self):
        super().math_operation()
        result=self.num1*self.num2
        print(result)
        
print("Addition is: ")
addobj=parent_A(2,5)
addobj.math_operation()
print("mulltiplication is: ")
addobj=child_B(2,5)
addobj.math_operation()     
        
