from math import fabs


print(f'not False: {not False}')
print(f'not True: {not True}')
print()

"""
Tabela verdade (and):

V and V == True
V and F == False
F and V == False
F and F == False
"""
print(f'V and V: {True and True}')
print(f'V and F: {True and False}')
print(f'F and V: {False and True}')
print(f'F and F: {False and False}')
print()

"""
Tabela verdade (or):
V or V == True
V or F == True
F or V == True
F or F == False
"""
print(f'V or V: {True or False}')
print(f'V or F: {True or False}') 
print(f'F or V: {False or True}')
print(f'F or F: {False or False}')
