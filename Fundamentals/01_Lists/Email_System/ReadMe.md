## Email System (Core Python – String & List Operations)
---
## Overview

This project is a menu-driven Python program that performs structured preprocessing on a list of email addresses. The focus of this system is string manipulation, duplicate handling without sets, and list-based data cleaning — simulating basic real-world preprocessing tasks.

## Dataset Used

emails = ["aj@gmail.com","  rahul@yahoo.com ","tina@outlook.com","aj@gmail.com"]

## Features Implemented

The system allows the user to:

- Remove extra spaces from email addresses
- Extract usernames (text before @)
- Identify duplicate usernames with frequency count
- Remove duplicate usernames (without using sets)
- Sort usernames alphabetically
- Count how many times a specific username appears

## Functional Design

Each operation is implemented as a separate function:

- remove_extra_spaces() → Cleans whitespace using .strip()
- extract_usernames() → Extracts username using .split("@")
- duplicate_elimination() → Removes duplicates using list membership logic
- duplicates() → Counts frequency using .count()
- sort_usernames() → Returns sorted list
- count_appearance() → Counts specific username occurrences
- User interaction and menu handling are managed inside main().

## Concepts Practiced

- String methods (.strip(), .split())
- List iteration
- Manual duplicate removal (without sets)
- Frequency counting using .count()
- Dictionary creation for tracking duplicates
- Menu-driven loop using while True
- Separation of logic into modular functions

## Constraints Followed

- No set() used for duplicate removal
- List methods used for transformations
- String methods used appropriately
- Manual duplicate elimination logic implemented

## Future Improvements (Version 2 Plan)

- Add email format validation
- Handle case sensitivity (AJ vs aj)
- Add exception handling
- Remove repeated calls to extract_usernames() for optimization
- Add unit testing
- Convert into file-based input system

## Purpose

This project is part of my structured foundation-building in Python, focusing on preprocessing techniques that are directly relevant to data cleaning and preparation in data science workflows.
The emphasis is on understanding core logic without relying on shortcuts like sets.

---
---