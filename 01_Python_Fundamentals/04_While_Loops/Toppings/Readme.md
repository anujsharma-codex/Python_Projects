# Pizza Toppings 

## Overview-

This program demonstrates the use of a sentinel-controlled while loop to collect user input until a termination condition is met.
The user is prompted to enter pizza toppings one by one.
Each valid topping is acknowledged immediately, and input continues until the user enters the sentinel value quit.

## What This Program Demonstrates-

- Sentinel values to control loop termination
- Real-time user feedback inside loops
- List accumulation from user input
- Clean separation between termination logic and data handling
- Proper loop exit and summary reporting

## Program Behavior-

1. Continuously prompts the user for pizza toppings.
2. Stops input when the user enters quit.
3. Rejects empty inputs.
4. Confirms each topping as it is added.
5. Displays a numbered list of all selected toppings at the end.

## Key Concepts Used-

- while True loop
- Sentinel value ("quit")
- List operations (append)
- Conditional branching
- Input cleanup using .strip()
- Iteration with enumerate()

## Scope-

- This program is intentionally small and focused.
  Its purpose is to demonstrate control-flow correctness and clean loop behavior, not complexity.