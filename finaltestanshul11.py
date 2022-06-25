
# Write a function that takes a list and a number as argument and 
# returns the number of times it appears in the list. 
# Use this function to find the most frequent number in [1, 1, 2, 1, 3, 1, 6, 2, 1, 2, 1]. 
# If the number provided is not in the list then end the program gracefully. 
# The output should be as follows, "1 is most frequent, appearing 6 times".

def getFrequency(list, x):
    count = 0
    for num in list:
        if x == num:
            count +=1
    if count == 0:
        print('The Number ' + str(x) + ' does not appear in the list.')
    else:
        print(str(x) + ' is most frequent, appearing ' + str(count) + ' times.')

lst = [1, 1, 2, 1, 3, 1, 6, 2, 1, 2, 1]
getFrequency(lst, 1)
