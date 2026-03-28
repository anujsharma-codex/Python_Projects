# Exception Handling – Fundamentals

## Overview

This folder contains exercises focused on understanding and implementing exception handling in Python.

The goal is to build programs that:

1. Don’t crash unexpectedly
2. Handle invalid user input gracefully
3. Recover from runtime errors
4. Provide meaningful feedback
5. Exception handling is what separates toy scripts from real software.

## Concepts Covered

### 1️⃣ Basic try-except

Handling common runtime errors such as:

- ZeroDivisionError
- ValueError
- FileNotFoundError
- Understanding how to prevent program - termination due to invalid operations.

### 2️⃣ Handling User Input Errors

Validating input where:

- Users enter strings instead of numbers
- Users enter unexpected formats
- Division by zero might occur
- Learning how to re-prompt users instead of - letting the program fail.

### 3️⃣ Using else

- Understanding the correct structure:
- This builds clean logical separation.

### 4️⃣ Using finally

Ensuring critical cleanup actions happen:

- Closing files
- Releasing resources
- Confirming execution steps
- Even when errors occur.

### 5️⃣ Handling File Exceptions

Managing:

- Missing files
- Incorrect file paths
- Unexpected file errors

Essential for real-world data science where file corruption or wrong paths are common.

## Skills Strengthened

- Defensive programming mindset
- Writing resilient CLI applications
- Understanding Python’s error hierarchy
- Separating normal logic from failure logic
- Improving UX by handling errors properly

## Why This Matters for Data Science

### In real projects:

- Datasets are missing columns

- Files are corrupted
- APIs fail
- Users input wrong parameters
- Models receive invalid values
- If your code crashes during these situations, you are not industry-ready.

Strong exception handling:

- Makes your ML pipelines stable
- Prevents silent failures
- Improves debugging
- Makes production systems reliable