#!/usr/bin/env python3
import sys

def is_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def main(digit):
    count = 0
    for num in range(10000):
        if is_prime(num) and digit in str(num):
            print(num)
            count += 1
    print(f"Total count: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./primos.py <digit>")
        sys.exit(1)
    main(sys.argv[1])
