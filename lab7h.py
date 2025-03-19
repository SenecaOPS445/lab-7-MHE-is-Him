#!/usr/bin/env python3
# Student ID: mhamilton-edwards

def function1():
    print('print() in function1 on schoolName:', schoolName)

def function2():
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca College'
print('print() in main on schoolName:', schoolName)
function1()  # This will print the global schoolName 'Seneca College'
print('print() in main on schoolName:', schoolName)  # This will print the same global schoolName
function2()  # This will print the global schoolName 'Seneca College'
print('print() in main on schoolName:', schoolName)  # This will print the same global schoolName
