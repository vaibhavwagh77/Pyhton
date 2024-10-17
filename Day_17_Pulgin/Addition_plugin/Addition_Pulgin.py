from pulgin import pluginInterface
class additionPlugin(pluginInterface):
    def execute(self,a,b):
        return a+b


if __name__=="__main__":
    print(__name__)
    add_pulgin= additionPlugin()
    result=add_pulgin.execute(10,20)
    print(f"The sum is {result}")