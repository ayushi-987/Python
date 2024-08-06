# Python Subprocess Modules

'''
Reason for this module is you cannot store the value of os module command
subprocess.Popen()
shell = True/False avoid shell = True
'''

import subprocess

# Define the command to be executed
command = ["ls", "-l"]

# Create a subprocess to execute the command
sp = subprocess.Popen(
    command,                  # Command to execute
    shell=True,               # Whether to use the shell (not needed for list commands)
    stdout=subprocess.PIPE,   # Redirect the standard output (stdout) to a pipe
    stderr=subprocess.PIPE,   # Redirect the standard error (stderr) to a pipe
    universal_newlines=True   # Use universal newlines mode (returns output as a string)
)

# Wait for the subprocess to complete
rt = sp.wait()

# Retrieve the output and error messages from the subprocess
out, err = sp.communicate()

# Print the output and error messages
print(out)
print(err)
