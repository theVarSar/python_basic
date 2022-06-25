# Write a cheating program, in which the user input is returned with the following modifications. 
# 1. The first letter of every word is replaced by the letter that precedes it in the English alphabetical order. 
# 2. The last letter of every word is replaced by the letter succeeding it in the English alphabetical order. 
# 3. If the user enters a number, then replace it with the sign that is alternative to it on the main keyboard 
# (and gets activated by pressing numbers with shift key). 
# 4. And if the user enters any of the sign, then replace that with the corresponding number or alphabet on the keyboard. 
# For example, if the user input is "I am Python!", then the expected output is "H zn Oythoo1".

import string
line = input("Enter a string: ")
line = line.translate(line.maketrans('', '', string.punctuation))
line = line.rstrip()
line2 = str()
words = line.split()
lwrCase = list(string.ascii_lowercase)
UprCase = list(string.ascii_uppercase)
# nums = list(string.digits)
# splChar = list([")", "!","@","#", "$", "%", "^","&", "*", "("])
for word in words:
    fchar = str()
    lchar = str()

    if word[:1].islower():
        fchar = lwrCase[lwrCase.index(word[:1])-1]
    else:
        fchar = UprCase[UprCase.index(word[:1])-1]

    if len(word) > 1:
        if word[-1:].islower():
            lchar = lwrCase[lwrCase.index(word[-1:])+1]
        else:
            lchar = UprCase[UprCase.index(word[-1:])+1]
        
    word = fchar[:] + word[1:-1] + lchar[:]
    line2 = line2 + word + " "
print(line2)