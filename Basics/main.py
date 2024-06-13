print("Hello world!")

# Variables and Data Types
x = 5
y = "Hello"
z = 3.14

print(x, y, z)

# Lists and Tuples
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)

print(my_list)
print(my_tuple)

#Control Structure
x = 10
if( x > 5):
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

for i in range(1,5):
    print(i)

while x > 0:
    print(x)
    x -= 1

# Functions

def add_numbers(a,b):
    return a + b

result = add_numbers(10,5)
print(result)

# File Handling
with open("example.txt","w") as file:
    file.write("Hello, world!")

with open("example.txt","r") as file:
    content = file.read()
    print(content)