import re


with open("madlibs.txt", "r") as file:
    line = file.read()
    for word in line.split():
        if "ADJECTIVE" in word:
            input_adj = input("Enter an adjective:")
            line = re.sub("ADJECTIVE", input_adj, line, 1)
        if "VERB" in word:
            input_verb = input("Enter a verb:")
            line = re.sub("VERB", input_verb, line, 1)
        if "NOUN" in word:
            input_noun = input("Enter a noun:")
            line = re.sub("NOUN", input_noun, line, 1)
    print (line)
with open("output.txt", "w") as out:
    out.write(line)

