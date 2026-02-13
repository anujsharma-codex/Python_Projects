# Data Cleanup System (Core Python – List Operations)
---
## Overview

This project is a menu-driven Python program that performs fundamental list operations on a dataset.

It is designed to demonstrate:

Function modularity
List manipulation
Clean logic separation
Basic program structuring
This is part of my Python foundation-building phase.

## Dataset Used

Data = [10, 20, -5, 30, -2, 40, 20, 50]

## Features

The program allows the user to:

- Remove all negative numbers
- Count how many times a number appears
- Insert a number before/after a target number
- Reverse the list
- Create a sorted copy (without modifying original list)
- Check whether a number exists in the list

## Project Structure

The program follows a modular design:

1. Each operation is implemented as a separate function.
2. User interaction is handled inside main().
3. Logic and input/output are separated for better reusability.

## Concepts Practiced

Lists and list methods

- .count()
- .insert()
- .copy()
- sorted()
- Membership operator (in)
- Function parameters and return values
- Menu-driven loop using while True

## Design Decisions

- Functions are reusable and independent of user input.
- The original dataset resets every loop iteration to simulate stateless execution.
- A sorted copy is created without modifying the original list.

## Future Improvements (Version 2 Plan)

1. Add exception handling (try/except)
2. Add support for floats and mixed data types
3. Add input validation
4. Add persistent data storage (file handling)
5. Add unit tests

## Purpose

This project is part of my structured progression toward data science and software development.
The focus is on building strong fundamentals before layering SQL, data analysis libraries, and machine learning.

---
---