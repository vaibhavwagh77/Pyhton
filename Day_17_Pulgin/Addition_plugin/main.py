from Day_17_Pulgin.Addition_plugin.Addition_Pulgin import additionPlugin


def main():
    add_plugin = additionPlugin()
    value1=int(input("Enter the first number: "))
    value2=int(input("Enter the second number: "))
    result=add_plugin.execute(value1,value2)
    print(f"The sum of {value1} and {value2} is: {result}")

if __name__=="__main__":
    main()