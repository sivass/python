# List Comprehension
squares = [x**2  for x in range(10)]
print(squares)

#Dictionaries
my_dict = { k:v for k, v in zip(['a', 'b', 'c'], [1, 2, 3])}
print(my_dict)

#Advanced Functions
def apply_func(func, x):
    return func(x)

def square(x):
    return x ** 2

result = apply_func(square,5)
print(result)

# Lambda Functions
add = lambda a,b: a + b
print(add(3,5))


#Object-oriented Programming
class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
person = Person("Alice", 30)
print(person)


# Error Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: division by zero")