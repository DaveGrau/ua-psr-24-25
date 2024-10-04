import readchar
def printAllPreviousChars():
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

def main():
    printAllPreviousChars()

if __name__ == "__main__":
    main()
    
