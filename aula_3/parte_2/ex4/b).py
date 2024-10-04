import readchar
def printAllPreviousChars():
    print(f"Initialized printAllPreviousChars()")
    key = readchar.readkey()
    char = readchar.readchar()
    while True:
        char = readchar.readchar()
        if char != " ":
            break # Only accepts non blank values

    
    print(f"The key introduced was {key}")
    print(f"Char {char} was introduced")
    print(f"Now in order of ascii values")
    
    ascii_value = ord(char)
    
    for i in range(32, ascii_value + 1):
        print(chr(i), end=" ")
    print()
    
    pass

def readAllUpTo(stop_char):
    print(f"Initialized readAllUpTo()")
    print(f"You must type {stop_char} to end the program")
    while True:
        char = readchar.readchar()
        if char == stop_char:
            break
        print(f"{char} was typed, but the correct one is {stop_char}")
    print(f"You've typed the correct char!")
    pass

def main():
    printAllPreviousChars()
    readAllUpTo("p")

if __name__ == "__main__":
    main()
    
