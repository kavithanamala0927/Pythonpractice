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
