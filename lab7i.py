#!/usr/bin/env python3
# Student ID: mhamilton-edwards

def function1():
    global schoolName  # This ensures we modify the global schoolName
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # This ensures we modify the global schoolName
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()  # This will modify the global schoolName to 'SICT'
print('print() in main on schoolName:', schoolName)  # Now it should print 'SICT'
function2()  # This will modify the global schoolName to 'SSDO'
print('print() in main on schoolName:', schoolName)  # Now it should print 'SSDO'
