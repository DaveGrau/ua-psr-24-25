#!/usr/bin/env python3

maximum_number = 100

def isPerfect(value):
    sum = 0
    if value == 1:
        num = 1
    else:
        num = int(value/2)
        
    for i in range(1, num +1):
        if value%i == 0:
            sum += i
    if sum == value:
        return True
    return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(0, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()