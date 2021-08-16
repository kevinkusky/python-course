# *********************************************
# Import statements in python

import random

# How does python search?

# sys - built-in module to python with a path attribute
import sys

# Returns a list of paths python searches
# when importing a module
# Note: first string is always directory/module executed in
#              - empty if executed in REPL
# Will iterate through list and look for module imported
print(sys.path)

# ********************************
# pythonpath environment variable
# PYTHONPATH=/home/appacademy

# by specifiying a path, path will be inserted into
# sys.path after the first entry - dir executed in
# ********************************

# Relative imports
# *****ONLY IN FROM SYNTAX*****

# . - same dir as where import statement is
# .. - 2 looks at the dir above import statement

# from .mymodule import MyClass

# *********************************************


# *********************************************
# Modules

# 2 Types

# Directories
#     - To be Module; Must Contain: 
#            -__init__.py - initializes dir module when imported or executed as a program
#                           ***runs first when module in directory is invoked***
#            -__main__.py - runs if it is invoked as a program

# Files - All files are modules


# Invoked 2 Ways

# Script
#        python my_package/my_module.py

# Module
#        python -m my_package.my_module
# *********************************************