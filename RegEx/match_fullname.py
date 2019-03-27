"""
How would you write a regex that matches the full name of someone
whose last name is Nakamoto? You can assume that the first name that
comes before it will always be one word that begins with a capital letter.
The regex must match the following:
• 'Satoshi Nakamoto'
• 'Alice Nakamoto'
• 'RoboCop Nakamoto'
but not the following:
• 'satoshi Nakamoto' (where the first name is not capitalized)
• 'Mr. Nakamoto' (where the preceding word has a nonletter character)
• 'Nakamoto' (which has no first name)
• 'Satoshi nakamoto' (where Nakamoto is not capitalized)
"""
import re


def match_fullname(names_list):
    pattern = "^[A-Z]\w+\s+[A-Z]\w+$"
    for name in names_list:
        search = re.search(pattern, name)
        if search:
            print ("Fullname matched:", name)
        else:
            print ("Fullname not matched:", name)

names_list = ['Satoshi Nakamoto', 'Alice Nakamoto', 'RoboCop Nakamoto',
    'satoshi Nakamoto', 'Mr. Nakamoto', 'Nakamoto', 'Satoshi nakamoto']
match_fullname(names_list)
