def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
       
        user_input = int(input("Enter an integer: "))
        
        result = is_prime(user_input)
        if result:
            print("It is a prime number.")
        else:
            print("Not prime.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()