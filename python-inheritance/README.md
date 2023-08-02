# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

## General
- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

# Requirements
## Python Scripts
- Recommended editors: Visual studio code
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- The length of your files will be tested using wc

## Documentation
- Do not use the works import or from inside your comments, the checker will think you try to import some modules

## Task 0
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

- Prototype: def is_same_class(obj, a_class):
- You are not allowed to import any module

## Task 1
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

- Prototype: *def is_kind_of_class(obj, a_class)*:
- You are not allowed to import any module

## Task 2
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

- Prototype: def inherits_from(obj, a_class):
- You are not allowed to import any module

## Task 3
Write an empty class BaseGeometry.

- You are not allowed to import any module

## Task 4
Write a class BaseGeometry (based on 3-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- You are not allowed to import any module

## Task 5
Write a class BaseGeometry (based on 4-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- Public instance method: def integer_validator(self, name, value): that validates value:
    - you can assume name is always a string
    - if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    - if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
- You are not allowed to import any module

## Task 6
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py).

- Instantiation with width and height: def __init__(self, width, height):
    - width and height must be private. No getter or setter
    - width and height must be positive integers, validated by integer_validator

## Task 7
Write a class Rectangle that inherits from BaseGeometry (5-base_geometry.py). (task based on 6-rectangle.py)

- Instantiation with width and height: def __init__(self, width, height)::
    - width and height must be private. No getter or setter
    - width and height must be positive integers validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

## Task 8
Write a class Square that inherits from Rectangle (7-rectangle.py):

- Instantiation with size: def __init__(self, size)::
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator
- the area() method must be implemented