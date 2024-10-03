def greet (name, message="hello"):
    print(f"{message},{name}")


#with default Argumnets

greet("allice")
greet("bob","hi")
greet(name="alice", message="good morning")
greet(message="hi", name="bob")
greet("hi","allice")
