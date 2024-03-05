#Ask the user to type in their favourite school subject. Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.

import csv

file = open("Books.csv","a")

title = input("Enter a title: ")

author = input("Enter author: ")

year = input("Enter the year it was released: ")

new_record = title + "," + author + "," + year + "\n"

file.write(str(new_record))

for row in file:
    print(row)

file.close()