import re

def validate_password(password):
    pattern = r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[ !\"#$%&'()*+,-.\/:;<=>?@^_`{|}~]).{8,32})"
    password_strength = re.search(pattern, password)
    if password_strength:
	    print ("The password entered is strong and it's a valid")
    else:
	    print ("Not a valid password")
		
validate_password("Arjungowri@719")
