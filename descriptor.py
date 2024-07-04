class PositiveInt:
    def  __init__(self, name) -> None:
        self.name = name 
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, int) or value < 0 or value > 120:
            raise TypeError(f"{self.name} must be a positive integer between 0 and 120")
        
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Person:
    age = PositiveInt('age')

    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age

p = Person('Ruslan', 14)
p.age = 15
print(p.age)





    
        