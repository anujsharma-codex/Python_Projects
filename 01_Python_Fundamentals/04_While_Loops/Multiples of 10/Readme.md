# Multiples of Ten 

## Overview-

This program demonstrates correct use of a sentinel-controlled while loop combined with input validation.
The user is repeatedly prompted to enter an integer.
The program reports whether the number is a multiple of 10 and continues until the user chooses to stop by pressing Enter.

## What This Program Demonstrates-

- When and why to use a while loop
- Sentinel values to control loop termination
- Defensive input handling using try / except
- Clean separation between input parsing and logic
- Clear, predictable program flow

## Program Behavior-

1. Accepts integer input from the user
2. Terminates cleanly when the user presses Enter without input
3. Rejects invalid (non-numeric) input without crashing
4. Reports whether a number is divisible by 10

## Key Concepts Used-

- while True loop
- Sentinel value (empty input)
- Exception handling (ValueError)
- Modulus operator (%)
- String cleanup with .strip()

## Scope-

This program is intentionally small and focused.
It is designed to demonstrate control flow correctness, not complexity.