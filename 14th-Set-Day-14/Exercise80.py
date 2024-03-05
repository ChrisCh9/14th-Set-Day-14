#Ask the user to enter their first name and then display the length of their first name. Then ask for their surname and display the length of their surname. Join their first name and surname together with a space between and display the result. Finally, display the length of their full name (including the space). 

import csv

file = open("Books.csv","w")

new_record = "To Kill A Mockingbird, Harper Lee, 1960\n"

file.write(str(new_record))

new_record = "A Brief History of Time, Stephen Hawking, 1980\n"

file.write(str(new_record))

new_record = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"

file.write(str(new_record))

new_record = "The Man who Mistook his Wife for a hat, Oliver Sacks, 1985\n"

file.write(str(new_record))

new_record = "Pride and Prejudice, Jane Austen, 1813\n"

file.write(str(new_record))

file.close()