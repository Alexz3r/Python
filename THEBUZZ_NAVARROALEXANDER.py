#Navarro Alexander John V.
#BSCS 2-A
def number_sequence(integer):
    for num in range(1, integer + 1):
        print(num, "Susunod..." if num % 2 else "Tito Boy!!!")

user_integer = int(input("Enter an integer: "))
number_sequence(user_integer)
