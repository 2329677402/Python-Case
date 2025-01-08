#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@ Date        : 01/07/2025 3:59 PM
@ Author      : Poco Ray
@ File        : hello.py
@ Description : This is a simple Python script that prints "Hello, World!" to the console.
"""

# 1. Basic Usage
print("Hello, World!")  # Hello, World!

# 2. Print multiple contents
print("Hello", "World", "Python")  # Hello World Python

# 3. Customize separator(Via sep parameter, default is space)
print("Hello", "World", "Python", sep="-")  # Hello-World-Python

# 4. Customize end(Via end parameter, default is newline)
print("Hello", end=" ")
print("World")
# Hello World

# 5. Print formatted string (formatted output)
# ① Use % to format string
name = "Alice"
age = 25
print("Name: %s, Age: %d" % (name, age))
# Name: Alice, Age: 25

# ② Using f-string (recommended)
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
# Name: Alice, Age: 25

# 6. Controls floating-point precision(Via format string)
pi = 3.14159265359
print(f"Pi to 2 decimal places: {pi:.2f}")  # Pi to 2 decimal places: 3.14

# 7. Print to file, Instead of console(Via file parameter)
with open("output.txt", "w") as f:
    print("Hello, World!", file=f)

# 8. Print complex objects such as dict, list, etc
data = {"name": "Alice", "age": 25}
print(data)  # {'name': 'Alice', 'age': 25}

# 9. Print multiple lines
print("""Hello,
This is a multi-line
print statement""")
# Hello,
# This is a multi-line
# print statement

# 10. Refresh Output(Via flush parameter)
print("Loading...", end="", flush=True)
import time

time.sleep(2)
print(" Done!")

# 11. Conditional output
x = 10
print("Hello, World!") if x > 5 else print("Goodbye, World!")

# 12. Print the text with color(pip install colorama)
from colorama import Fore, init

init()  # Cross-platform settings
print(Fore.RED + "Hello, World!" + Fore.RESET)  # Red text

# print("\033[1;31;40m Hello, World!")  # Red text on black background
