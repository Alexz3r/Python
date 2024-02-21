#Navarro Alexander John V.
#BsCs 2-A

# Let the user input values
name = input("Enter Name: ")
year = int(input("Enter year: "))
course = input("Enter your course: ")
location = input("Enter location: ")

# Print the fortune using string formatting
# i use "f" to convert it into string

fortune = f" {course} {name} {year}  {location}"



print("The following values are : " + fortune)
