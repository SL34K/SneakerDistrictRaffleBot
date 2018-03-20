#!/usr/bin/python
#.------..------..------..------..------.
#|S.--. ||L.--. ||3.--. ||4.--. ||K.--. |
#| :/\: || :/\: || :(): || :/\: || :/\: |
#| :\/: || (__) || ()() || :\/: || :\/: |
#| '--'S|| '--'L|| '--'3|| '--'4|| '--'K|
#`------'`------'`------'`------'`------'
#https://twitter.com/SL34K
#https://github.com/SL34K
#00110001 00110011
#00110000 00110011
#00110001 00111000 
#########################################
import csv
csv_row = []
usernames = []
try:
    for line,line_num in enumerate(open("100_followers.csv", 'rb')):
        csv_row.append(line_num.split())
        test = csv_row[line][0].decode('UTF-8')
        usernames.append((test.split(',')[1][1:-1]))
f = open("usernames.txt",'a')
for i in usernames:
    f.write(i+'\n')
    f.close() 
    print("Saved to usernames.txt")

