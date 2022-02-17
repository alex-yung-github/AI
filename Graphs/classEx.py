class Person:
    name = ""
    def __init__(self, name = None):
        self.name = name
    
    def say_hi(self):
        print("Hello, my name is", self.name)
    
p = Person("Jake")

p.say_hi()

