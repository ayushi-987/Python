# Sys module has to do nothing with the operating system, It handles the functions of python runtime environment.

import sys

sys.version    # Gives the version of python 
'''
Output:-
'3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)]'
'''

sys.platform   # Platform binaries presents
'''
Output:-
Linux
'''

sys.path  # Path of python files
'''
Output:-
['', 'C:\\Users\\ayushson\\AppData\\Local\\Programs\\Python\\Python312\\python312.zip', 'C:\\Users\\ayushson\\AppData\\Local\\Programs\\Python\\Python312\\DLLs', 'C:\\Users\\ayushson\\AppData\\Local\\Programs\\Python\\Python312\\Lib', 'C:\\Users\\ayushson\\AppData\\Local\\Programs\\Python\\Python312', 'C:\\Users\\ayushson\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages']
'''

sys.modules  # Returns all the python available modules
'''
Output:-
{'sys': <module 'sys' (built-in)>, 'builtins': <module 'builtins' (built-in)>,}
'''

sys.exit()   # It stops the execution of python script

sys.argv     # It lets you to return the arguements after file execution
print(sys.argv[1])
