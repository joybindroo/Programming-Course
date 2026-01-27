# Module 2: Programming Fundamentals

## Variables and Data Types

### Declaring and Assigning Variables

Variables are containers for storing data values. In programming, you need to declare a variable before using it, which involves giving it a name and optionally an initial value.

```python
# Variable declaration and assignment
name = "John"
age = 25
height = 5.9
is_student = True
```

### Primitive Data Types

Primitive data types are the basic building blocks of data manipulation:

- **Integers:** Whole numbers (positive, negative, or zero)
  - Example: `42`, `-17`, `0`
- **Floating-point numbers:** Numbers with decimal points
  - Example: `3.14`, `-2.5`, `0.001`
- **Characters:** Single alphanumeric characters
  - Example: `'A'`, `'b'`, `'7'`
- **Booleans:** Logical values representing true or false
  - Example: `True`, `False`

### Complex Data Types

Complex data types can hold multiple values or more complex structures:

- **Strings:** Sequences of characters enclosed in quotes
  - Example: `"Hello, World!"`, `'Programming'`
- **Arrays:** Ordered collections of elements of the same type
  - Example: `[1, 2, 3, 4, 5]`, `["apple", "banana", "orange"]`

## Control Flow

### Conditional Statements

Conditional statements allow your program to make decisions based on different conditions:

#### If-Else Statements
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

#### Switch-Case Statements
```python
day = "Monday"

switch (day):
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost weekend!")
    default:
        print("Regular day")
```

### Loops

Loops allow you to execute code repeatedly:

#### For Loops
Used when you know how many times you want to iterate:
```python
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

#### While Loops
Used when you want to continue until a condition is no longer true:
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

#### Do-While Loops
Similar to while loops, but always execute at least once:
```python
count = 0
do:
    print(count)
    count += 1
while count < 5
```

## Functions

### Defining and Calling Functions

Functions are reusable blocks of code that perform specific tasks:

```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

### Function Parameters and Return Values

Functions can accept input (parameters) and return output (return values):

```python
def add_numbers(a, b):
    sum_result = a + b
    return sum_result

def calculate_area(length, width):
    area = length * width
    return area

# Using functions with parameters
result = add_numbers(5, 3)  # Returns 8
room_area = calculate_area(10, 12)  # Returns 120
```

Functions can also have default parameter values:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("John"))  # Uses default greeting: Hello, John!
print(greet("Jane", "Hi"))  # Uses custom greeting: Hi, Jane!
```

## Input and Output

### Reading Input from the User

Getting input from users allows your programs to be interactive:

```python
# Reading string input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Reading numeric input
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

### Printing Output to the Console

Displaying output to users:

```python
# Basic printing
print("Hello, World!")

# Printing variables
name = "Alice"
age = 25
print(name, age)

# Formatted output
print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format(name, age))
```

## Practice Exercises

1. Create a program that asks for the user's age and tells them if they can vote
2. Write a function that calculates the area of a circle
3. Create a loop that prints numbers from 1 to 100, but only even numbers
4. Build a simple calculator that takes two numbers and an operator as input
5. Write a program that converts temperature from Celsius to Fahrenheit

## Key Takeaways

- Variables store data and have specific data types
- Control flow statements allow programs to make decisions and repeat actions
- Functions organize code into reusable blocks
- Input/output operations enable user interaction
- Master these fundamentals before moving to more complex topics