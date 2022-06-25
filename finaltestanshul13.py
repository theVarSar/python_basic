# Given a file “expenses.txt” containing comma separated track of expenses 
# in this format - DATE, EXPENSE, REASON , 
# write a program to find the total expenses by month. 
# The output should show the month followed by a '#' for each 100 Rs spent. 
# For example if in Feb 2018 total expense was 480, then the output line for that month will be "2018-02: ####" 

fhand = open('expenses.txt')

dct = dict()
for line in fhand:
    line = line.rstrip()
    if "," not in line:
        break
    list = line.split(',')
    month = list[0][:-3]
    if month not in dct:
        dct[month] = int(list[1])
    else:
        dct[month] = int(dct[month]) + int(list[1])

for key, val in list(dct.items()):
    print(key, ":", val)