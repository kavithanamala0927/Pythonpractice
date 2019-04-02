import re
import os
import sys


folder_path = "C:\\Users\\Z003YN0Y\\Desktop\\Files"
pattern = "(([\w\d]*).txt$)"
input_pattern = input("Enter pattern:::")
try:
    if re.compile(input_pattern):
        print ("Pattern is valid")
except:
    print ("Invalid pattern plz enter valid pattern and try...!!!")
    sys.exit(1)
match_lines = []
FOUND = 0
TXT_FILES = 0
for files in os.listdir(folder_path):
    search = re.search(pattern, files)
    if search:
        TXT_FILES = 1
        filename = os.path.join(folder_path, search.group())
        with open(filename, "r") as file:
            for lines in file.readlines():
                search = re.search(input_pattern, lines)
                if search:
                    FOUND = 1
                    match_lines.append(lines)
if not TXT_FILES:
    print ("No TXT files present in the directory")

if FOUND:
    print ("Pattern matches with the follwing lines:::")
    for line in match_lines:
        print (line)
else:
    print ("No macth pattern found")


