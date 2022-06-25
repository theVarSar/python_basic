# Write a program that reads the file "mistakes.txt" and  uses lists 
# list_1 = ['implimentation', 'beter', 'obvius', 'ambiguty', 'practicalty', 'readabilty'] and 
# list_2 =['implementation', 'better', 'obvious', 'ambiguity', 'practicality', 'readability'] 
# to transform the text in "mistakes.txt" into new text by replacing each occurrence 
# of a word list_1[i] by the corresponding word list_2[i]. 
# You may assume that all words are separated by white space and that letter case need not be preserved. 
# Then save the corrected text in a new file called "corrections.txt".

import string
fhand = open('mistakes.txt')
list_1 = ['implimentation', 'beter', 'obvius', 'ambiguty', 'practicalty', 'readabilty'] 
list_2 =['implementation', 'better', 'obvious', 'ambiguity', 'practicality', 'readability']

fout = open('corrections.txt', 'w')


for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.rstrip().lower()
    line2 = str()
    words = line.split()
    for word in words:
        if word in list_1:
            line2 = line2[:] + list_2[list_1.index(word)] + " "
        else:
            line2 = line2[:] + word + " "
    line2 = line2[:] + "\n"
    fout.write(line2)

fout.close()
fhand.close()
