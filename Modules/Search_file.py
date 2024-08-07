# Comment out one of both the codes before running as 1. Find specific file in the directory & 2. File all the files end with some extension.

import os
import argparse

# Set up argument parser
my_parse = argparse.ArgumentParser(description='Reading directory path to find the file')
my_parse.add_argument("pathname", help='Please enter the directory name')
my_parse.add_argument("filesearch", help='Please enter the directory name')

# Parse arguments
args = my_parse.parse_args()

# Search for the file
for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file == args.filesearch:
            path=os.path.join(dirname,file)
            print(path)


'''
Command:-
 python3 search-file.py /etc sysctl.conf
Output:-
/etc/sysctl.conf
/etc/ufw/sysctl.conf
'''

import os
import argparse

# Set up argument parser
my_parse = argparse.ArgumentParser(description='Reading directory path to find the file')
my_parse.add_argument("pathname", help='Please enter the directory name')

# Parse arguments
args = my_parse.parse_args()

# Search for the file
for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file.endswith(".conf"):
            path=os.path.join(dirname,file)
            print(path)
