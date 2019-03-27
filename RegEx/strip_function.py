"""
Write a function that takes a string and does the same thing as the strip()
string method. If no other arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and
end of the string. Otherwise, the characters specified in the second argument
to the function will be removed from the string.
"""
import re


def strip_function(input_string, chars=" "):
    pattern = "^(" + re.escape(chars) + ")*([\w\d\S\s]*?)("+re.escape(chars)\
        + ")*$"
    search = re.search(pattern, input_string)
    if search:
        print ("Striped string:" + '"' + search.group(2) + '"')
    else:
        print ("Nothhing to strip in the input string:", input_string)
strip_function("^^^^   This is   ", chars="^")
