"""
How would you write a regex that matches a number with commas for
every three digits? It must match the following:
• '42'
• '1,234'
• '6,368,745'
but not the following:
• '12,34,567' (which has only two digits between the commas)
• '1234' (which lacks commas)
"""

import re


def commas_for_every_3_digits(input_list):
    pattern = "^\d{1,2}(,\d{3})*$"
    for number in input_list:
        search = re.search(pattern, number)
        if search:
            print ("Pattern matches: ", number)
        else:
            print ("Pattern not matched: ", number)

input_list = ['42', '1,234', '6,368,745', '12,34,567', '1234']
commas_for_every_3_digits(input_list)
