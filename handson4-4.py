# Open the file in write mode
with open("D:/handson4-4edited.txt", "w") as file:
    # Write the content to the file
    file.write("Indentation refers to the spaces at the beginning of a code line. While indentation in other programming languages is only a resource for readability, indentation in Python is mandatory.")

import os

# Specify the old and new file names
old_file = "D:/handson4-4edited.txt"
new_file = "D:/handson4-4.final.txt"

# Rename the file
os.rename(old_file, new_file)


print("File renamed successfully.")
