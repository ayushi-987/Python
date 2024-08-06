#Python Platform Module:- It acts similar to uname

import platform

# Get operating system name
os_name = platform.system()

# Get architecture
arch = platform.architecture()

# Get machine type
machine_type = platform.machine()

#Get complete details
unam = platform.uname()

#Get the release version
reles = platform.release()

#Get the python version
pyversion = platform.python_version()

#Get the python tuple version
pytuver = platform.python_version_tuple()

print(f"Operating System: {os_name}")
print(f"Architecture: {arch}")
print(f"Machine Type: {machine_type}")


'''
Will illustrate the example for this below:-
'''
import os
if platform.system() == "Linux":
    os.system("ls")
elif platform.system() == "Windows":
    os.system("dir")
else:
    print("Unsupported operating system") 