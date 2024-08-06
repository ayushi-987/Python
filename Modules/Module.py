#Python OS Modules

import os

dir(os.system)  # Give all the methods supported by os.system

os.system("ls -l")     # It give the exit code 0 if successful else results 1
'''
Output:-
total 4
drwxr-x--- 4 ubuntu ubuntu 4096 Aug  6 14:37 ubuntu
0
'''
x=os.system("ls -l")   # This doesn't returns exit code it just give the output and store the exit code to x
'''
Output:-
total 4
drwxr-x--- 4 ubuntu ubuntu 4096 Aug  6 14:37 ubuntu
'''
print(x)               # Will get the exit code
'''
Output:-
0
'''
os.getcwd()           # Run similar to os.system("pwd") "Current working directory"
'''
Output:-
'/home/ubuntu'
'''

os.chdir("/tmp")     # Change your working directory & No output

os.listdir()         #  List ls -l
'''
Output:-
['.ssh', '.bashrc', '.lesshst', '.profile', '.bash_logout', '.cache']
'''

for i in os.listdir():  # Give list of content
    print(i)
'''
Output:-
.ssh
.bashrc
.lesshst
.profile
.bash_logout
.cache
'''

os.listdir("/")    # list ls -l of that specific path
'''
Output:-
['var', 'bin', 'proc', 'media', 'lib', 'etc', 'opt', 'mnt', 'run', 'boot', 'srv', 'root', 'usr', 'lost+found', 'dev', 'bin.usr-is-merged', 'sbin', 'tmp', 'home', 'sys', 'snap', 'lib64', 'sbin.usr-is-merged', 'lib.usr-is-merged']
'''

os.mknod("testpython")  # Make the file in pwd
'''
Output:-
>>> os.listdir()
['testpython', '.ssh', '.bashrc', '.lesshst', '.profile', '.bash_logout', '.cache']
'''

os.mkdir("test")    # Make the directory in pwd
'''
Output:-
>>> os.listdir()
['testpython', 'test', '.ssh', '.bashrc', '.lesshst', '.profile', '.bash_logout', '.cache']
'''

os.makedirs("testnest/kin")  # Make the nesting directories  
'''
Output:-
>>> os.listdir()
['testpython', 'testnest', 'test', '.ssh', '.bashrc', '.lesshst', '.profile', '.bash_logout', '.cache']
'''

os.environ   # Give the environment variables
'''
Output:-
environ({'SHELL': '/bin/bash', 'PWD': '/home/ubuntu', 'LOGNAME': 'ubuntu', 'XDG_SESSION_TYPE': 'tty', 'HOME': '/home/ubuntu', 'LANG': 'C.UTF-8', 'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;
'''

os.environ.get("TERM")  # Get the specific environment variable
'''
Output:-
'xterm-256color'
'''

os.getuid()     # Get the uid of the system
'''
Output:-
1000
'''

os.rmdir("test")  # remove the directory

os.removedirs("test/test1") #remove nesting directories

os.rename("testpython", "py-thon") #rename the file


dir(os.path)  # List all the methods supported by os.path

os.path.exists("/etc/hosts")   # If the file exists or not
'''
output:-
true
'''

os.path.isfile("/etc/hosts")  #If path is the file or not
'''
output:-
true
'''

os.path.isdir("/etc/hosts")   #If it is the dir or not
'''
output:-
false
'''

os.path.islink("/etc")     #If it is the link or not
'''
output:-
false
'''

os.path.getsize("/etc/hosts")
'''
output:-
220
'''

os.path.basename("/etc/hosts")   # Get the base file name
'''
output:-
'hosts'
'''

os.path.dirname("/etc/hosts")   # Get the directory name
'''
output:-
'/etc'
'''

os.path.join("/home","testfile")   # join the paths
'''
output:-
'/home/testfile'
''' 

os.walk("/etc")    #   It create the generator file

list(os.walk("/etc"))   # It give the list like ("path" , "directory" , "files")
