#!/usr/bin/env python3

def isPrime(value):
    if value < 2:
        return False
    elif value//2 != 0:
        for i in range(2,int(value/2) +1):
            if value%i == 0:
                return False
        return True
        

def main():
    maximum_number = 50
    print("Starting to compute prime numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPrime(i):
            print('Number ' + str(i) + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')

    #for i in range(0, 10000):
        #if isPrime(i):
            
    
    
if __name__ == "__main__":
    # __name__ is a special variable
    # Python automatically sets its value to “__main__” if the script is being run directly
    main()