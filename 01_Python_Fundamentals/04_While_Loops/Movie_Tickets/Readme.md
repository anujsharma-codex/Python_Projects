# Movie Ticket Pricing 

## Overview-

This program calculates movie ticket prices based on a user’s age using a sentinel-controlled while loop and conditional branching.
The user is repeatedly asked for their age, and the program determines the ticket price according to predefined rules.
Input continues until the user chooses to exit by entering quit.

## What This Program Demonstrates-

- Sentinel values to control loop termination
- Defensive input handling using try / except
- Proper use of if / elif / else for rule-based logic
- Validation of invalid or unrealistic input
- Clear separation between input, validation, and business rules

## Ticket Pricing Rules-

1. Under 3 years → Free
2. 3 to 12 years → $10
3. Over 12 years → $15

## Program Behavior-

1. Prompts the user for their age repeatedly
2. Stops execution when the user enters quit
3. Rejects non-numeric input
4. Rejects invalid ages (zero or negative)
5. Displays the correct ticket price based on age

## Key Concepts Used-

- while True loop
- Sentinel value ("quit")
- Exception handling (ValueError)
- Conditional statements (if / elif / else)
- Input cleanup using .strip()

## Scope-

- This program is intentionally focused and minimal.
  Its goal is to demonstrate correct control flow and decision-making, not complexity.