"""
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength.
"""
import re


def validate_password(password):
    pattern = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[ !\"#$%&'()*+,-.\/:;" \
        "<=>?@^_`{|}~]).{8,32})"
    password_strength = re.search(pattern, password)
    if password_strength:
        print ("The password entered is strong and it's a valid")
    else:
        print ("Not a valid password")
validate_password("Arjungowri@719")
