#Q.1 Write a Python program to accept a number and check whether it is prime or not.

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Divisible by another number, not prime
    return True  # Prime number

# Accept a number from the user
number = int(input("Enter a number: "))

# Check if the number is prime or not
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Output:
Enter a number: 7
7 is a prime number.