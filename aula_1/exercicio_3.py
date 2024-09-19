import sys
from prime import is_prime
from colorama import Fore, Style

def main(value):
    for i in range(value + 1):
        if is_prime(i):
            print(Fore.GREEN + "Number " + str(i) + " is prime" + Style.RESET_ALL)
        else:
            print("Number " + str(i) + " is not prime")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 filename.py <number>")
        sys.exit(1)

    try:
        value = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)

    main(value)
