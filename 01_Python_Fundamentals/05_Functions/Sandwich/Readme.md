# Sandwich Maker

## Overview

This program demonstrates a clear and practical understanding of Python function parameters, specifically:

- Positional arguments
- Arbitrary positional arguments (*args)
- Arbitrary keyword arguments (**kwargs)

The goal is not user interaction or menus, but showing how flexible function interfaces are designed and used in Python.

## Concepts Demonstrated

1. Positional Arguments
  A required positional argument (bread) defines the base of the sandwich.
  sandwich_summary("Whole Wheat", ...)
  This enforces mandatory input and shows correct function design.

2. Arbitrary Positional Arguments (*args)
The *fillings parameter allows the function to accept any number of sandwich fillings without forcing the caller to pass a list.
  sandwich_summary("Sourdough", "Cheese", "Tomato", "Lettuce")
Internally, these values are collected into a tuple.

3. Arbitrary Keyword Arguments (**kwargs)
 Optional sandwich details (like oil, salt, grilling preference) are handled using keyword arguments.

sandwich_summary(
    "Ciabatta",
    "Paneer", "Onion",
    oil="less",
    grill=True)
These are collected into a dictionary, making the function extensible without changing its definition.

## Why This Approach Matters

Eliminates rigid parameter lists
Makes the function future-proof
Reflects how real-world APIs and libraries are designed
Builds a strong foundation for OOP concepts like flexible constructors (__init__)

## Key Takeaways

*args defaults to an empty tuple if no values are passed
**kwargs defaults to an empty dictionary if no values are passed
Functions can remain valid and safe even when optional arguments are omitted
Clean function signatures are more important than complex user input logic at this stage

## Purpose of This Exercise

This is a concept-focused implementation, not a full application.
It is part of a structured progression from Python fundamentals toward object-oriented programming and larger projects.