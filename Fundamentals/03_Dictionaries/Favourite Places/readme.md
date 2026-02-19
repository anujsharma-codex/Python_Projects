# Favorite Places Collector

## Description

This Python program collects and stores people’s favorite places using a dictionary of lists.
Each person’s name is used as a key, and their favorite places (from one to three) are stored as values in a list.
The program supports multiple users, allows early stopping while entering places, and displays the collected data in a clear, readable format.

## Objective

- Practice using dictionaries with list values
- Work with nested loops
- Handle user-driven input flow
- Display structured data cleanly

## Concepts Used

- Dictionaries
- Lists
- while loops
- Nested loops
- Dictionary iteration using .items()
- String methods: .strip(), .title()
- Conditional logic

## Program Flow

1. Initialize an empty dictionary favorite_places
2. Ask the user for their name
3. Ask the user to enter up to three favorite places
4. User can type done to stop early
5. Store the list of places against the user’s name
6. Ask if another person wants to enter data
7. After data entry is complete:
8. Loop through the dictionary
9. Print each person’s name and their favorite places