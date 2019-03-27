"""
How would you write a regex that matches a sentence where the first
word is either Alice, Bob, or Carol; the second word is either eats, pets, or
throws; the third word is apples, cats, or baseballs; and the sentence ends
with a period? This regex should be case-insensitive. It must match the
following:
 'Alice eats apples.'
 'Bob pets cats.'
 'Carol throws baseballs.'
 'Alice throws Apples.'
 'BOB EATS CATS.'
but not the following:
• 'RoboCop eats apples.'
• 'ALICE THROWS FOOTBALLS.'
• 'Carol eats 7 cats.'
"""
import re


def match_sentence(sentence_list):
    pattern = "^(Alice|Bob|Carol)\s*(eats|pets|throws)\s*"\
        "(apples|cats|baseballs)\.$"
    for sentence in sentence_list:
        search = re.search(pattern, sentence, re.IGNORECASE)
        if search:
            print ("sentence matched:", sentence)
        else:
            print ("sentence not matched:", sentence)
sentence_list = ['Alice eats apples.', 'Bob pets cats.',
'Carol throws baseballs.', 'Alice throws Apples.','BOB EATS CATS.',
'RoboCop eats apples.', 'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']
match_sentence(sentence_list)
