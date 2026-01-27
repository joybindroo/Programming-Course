# Module 3: Object-Oriented Programming (OOP)

## Core Concepts of OOP

### What is Object-Oriented Programming?

Object-Oriented Programming is a programming paradigm based on the concept of "objects," which can contain data and code. OOP models real-world entities and their interactions, making code more organized, reusable, and easier to maintain.

### Classes and Objects: Building Blocks of OOP

#### Classes

A class is a blueprint or template for creating objects. It defines properties (attributes) and behaviors (methods) that objects of that class will have.

**Example Class Definition:**
```python
class Car:
    # Class attributes
    wheels = 4
    
    # Constructor method
    def __init__(self, make, model, year):
        self.make = make      # Instance attribute
        self.model = model    # Instance attribute
        self.year = year      # Instance attribute
        self.is_running = False
    
    # Instance methods
    def start_engine(self):
        self.is_running = True
        print(f"The {self.make} {self.model}'s engine is running")
    
    def stop_engine(self):
        self.is_running = False
        print(f"The {self.make} {self.model}'s engine is stopped")
    
    def drive(self, distance):
        if self.is_running:
            print(f"Driving {distance} miles")
        else:
            print("Start the engine first!")
```

#### Objects

An object is an instance of a class. It has its own state and behavior defined by the class.

**Creating Objects:**
```python
# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)

# Using objects
car1.start_engine()  # Output: The Toyota Camry's engine is running
car1.drive(50)        # Output: Driving 50 miles

car2.drive(30)        # Output: Start the engine first!
car2.start_engine()
car2.drive(30)        # Output: Driving 30 miles
```

### Encapsulation: Data Hiding and Information Protection

Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit (class). It also involves restricting direct access to some of an object's components.

#### Public and Private Members

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number  # Public attribute
        self.__balance = initial_balance      # Private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")
    
    def get_balance(self):
        return self.__balance  # Controlled access to private data

# Usage
account = BankAccount("123456789", 1000)
account.deposit(500)    # Output: Deposited $500. New balance: $1500
account.withdraw(200)   # Output: Withdrew $200. New balance: $1300

# Can't directly access private attribute
# print(account.__balance)  # This would cause an error
print(account.get_balance())  # Output: 1300
```

### Inheritance: Creating Hierarchies of Classes

Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reuse and creates logical hierarchies.

#### Single Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # Call parent constructor
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} is barking")
    
    # Override parent method
    def eat(self):
        print(f"{self.name} the {self.breed} is eating dog food")

# Usage
dog = Dog("Buddy", "Golden Retriever")
dog.eat()      # Output: Buddy the Golden Retriever is eating dog food
dog.sleep()    # Output: Buddy is sleeping
dog.bark()     # Output: Buddy is barking
```

#### Multiple Inheritance

```python
class Flyable:
    def fly(self):
        print("Flying in the sky")

class Swimmable:
    def swim(self):
        print("Swimming in water")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack! Quack!")

# Usage
duck = Duck()
duck.fly()   # Output: Flying in the sky
duck.swim()  # Output: Swimming in water
duck.quack() # Output: Quack! Quack!
```

### Polymorphism: Code Reuse and Flexibility

Polymorphism allows objects of different classes to be treated as objects of a common parent class. It enables "one interface, multiple implementations."

#### Method Overriding

```python
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Polymorphic function
def print_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Usage
circle = Circle(5)
rectangle = Rectangle(4, 6)

print_shape_info(circle)     # Works for Circle
print_shape_info(rectangle)  # Works for Rectangle
```

#### Duck Typing

```python
class Guitar:
    def play(self):
        print("Playing guitar: Strum strum")

class Piano:
    def play(self):
        print("Playing piano: Plink plonk")

class Drum:
    def beat(self):
        print("Beating drums: Boom boom")

# Function that works with any object that has a play method
def perform(musician):
    musician.play()

# Usage
guitarist = Guitar()
pianist = Piano()
drummer = Drum()

perform(guitarist)  # Output: Playing guitar: Strum strum
perform(pianist)    # Output: Playing piano: Plink plonk
# perform(drummer)  # This would cause an error - no play method
```

## Designing Object-Oriented Systems

### Modeling Real-World Problems with OOP

#### Identifying Objects and Their Relationships

**Steps for OOP Design:**

1. **Identify Nouns:** Look for nouns in the problem description to identify potential classes
2. **Identify Verbs:** Look for verbs to identify potential methods
3. **Define Attributes:** Determine what properties each object needs
4. **Establish Relationships:** Define how objects interact with each other

**Example: Library Management System**

```
Problem: A library needs to track books, members, and loans.
Members can borrow books, and the system should track due dates.
```

**Identified Classes:**
- `Book`: Represents library books
- `Member`: Represents library members
- `Loan`: Represents book loans
- `Library`: Manages the overall system

### Creating Class Diagrams

Class diagrams visualize the structure and relationships between classes.

**Notation:**
- **Class Name:** Top compartment
- **Attributes:** Middle compartment
- **Methods:** Bottom compartment
- **Relationships:** Lines with symbols (inheritance: arrow, association: line)

**Example Class Diagram:**
```
+----------------+       +----------------+       +----------------+
|    Library     |       |      Book      |       |     Member     |
+----------------+       +----------------+       +----------------+
| -name: String  |       | -title: String |       | -name: String  |
| -address: Str  |       | -author: String|       | -member_id: Int|
| -books: List   |       | -isbn: String  |       | -loans: List   |
+----------------+       +----------------+       +----------------+
| +add_book()    |       | +get_title()   |       | +borrow_book() |
| +find_book()   |       | +is_available()|       | +return_book() |
| +register_member()|     | +checkout()    |       | +get_loans()   |
+----------------+       +----------------+       +----------------+
       |                         |                         |
       |1                        |*                        |*
       +-------------------------+-------------------------+
                          |
                     +-----------+
                     |    Loan   |
                     +-----------+
                     | -due_date:|
                     | -book:    |
                     | -member:  |
                     +-----------+
                     | +is_overdue() |
                     | +extend()     |
                     +-----------+
```

### Implementation Example

```python
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def checkout(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.checkout():
            self.borrowed_books.append(book)
            return True
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)

class Loan:
    def __init__(self, book, member, days=14):
        self.book = book
        self.member = member
        self.due_date = datetime.now() + timedelta(days=days)
        self.returned = False
    
    def is_overdue(self):
        return not self.returned and datetime.now() > self.due_date
    
    def extend(self, days=7):
        if not self.returned:
            self.due_date += timedelta(days=days)

class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.members = []
        self.loans = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def register_member(self, member):
        self.members.append(member)
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                return book
        return None
    
    def process_loan(self, member_id, book_title):
        member = next((m for m in self.members if m.member_id == member_id), None)
        book = self.find_book(book_title)
        
        if member and book:
            if member.borrow_book(book):
                loan = Loan(book, member)
                self.loans.append(loan)
                return f"Book '{book.title}' loaned to {member.name}"
            else:
                return "Book not available"
        return "Invalid member or book"

# Usage
library = Library("City Library", "123 Main St")

# Add books
book1 = Book("Python Programming", "John Smith", "123456789")
book2 = Book("OOP Concepts", "Jane Doe", "987654321")
library.add_book(book1)
library.add_book(book2)

# Register members
member1 = Member("Alice", "M001")
member2 = Member("Bob", "M002")
library.register_member(member1)
library.register_member(member2)

# Process loans
print(library.process_loan("M001", "Python Programming"))
print(library.process_loan("M002", "Python Programming"))  # Already borrowed
```

## OOP Design Principles

### SOLID Principles

1. **Single Responsibility Principle:** A class should have only one reason to change
2. **Open/Closed Principle:** Classes should be open for extension, closed for modification
3. **Liskov Substitution Principle:** Subtypes must be substitutable for their base types
4. **Interface Segregation Principle:** Clients shouldn't depend on interfaces they don't use
5. **Dependency Inversion Principle:** Depend on abstractions, not concretions

### Composition over Inheritance

```python
# Instead of deep inheritance hierarchies, use composition
class Engine:
    def start(self):
        print("Engine started")

class GPS:
    def navigate(self, destination):
        print(f"Navigating to {destination}")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
        self.gps = GPS()        # Composition
    
    def start_journey(self, destination):
        self.engine.start()
        self.gps.navigate(destination)

# This is more flexible than deep inheritance
```

## Practice Exercises

### Basic OOP Concepts
1. Create a `Person` class with name, age, and a `celebrate_birthday()` method
2. Implement a `BankAccount` class with deposit, withdraw, and balance checking
3. Create a hierarchy of shapes (Circle, Rectangle, Triangle) inheriting from a base `Shape` class

### Intermediate OOP
1. Design a simple e-commerce system with Product, Cart, and Customer classes
2. Implement a file system with File, Folder, and Directory classes
3. Create a game with Player, Enemy, and Game classes

### Advanced OOP
1. Design a restaurant management system with Order, MenuItem, Staff, and Customer classes
2. Implement a social media system with User, Post, Comment, and Notification classes
3. Create a simulation of a traffic system with Vehicle, Road, and TrafficLight classes

## Key Takeaways

- OOP models real-world entities using classes and objects
- Encapsulation protects data and controls access
- Inheritance promotes code reuse and creates logical hierarchies
- Polymorphism allows flexible code that works with different object types
- Good OOP design follows established principles like SOLID
- Composition is often more flexible than deep inheritance hierarchies
- Practice identifying objects, their attributes, and their relationships to design effective systems