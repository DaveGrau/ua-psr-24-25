from time import time, ctime
from colorama import *

def tic():
    global TIME
    TIME = time()
    return TIME

def toc():
    time_start = TIME
    now = time()
    time_difference = now - time_start
    print(f"Time taken: {Back.LIGHTMAGENTA_EX}{Style.BRIGHT}{Fore.RED}{time_difference}{Style.RESET_ALL}")
    return time_difference
    

def sqrt_number():
    init()
    print(Back.YELLOW + Style.DIM + Fore.GREEN + ctime() + Style.RESET_ALL)
    tic()
    import math
    for number in range(0, 50*10**(6) +1):
        sqrt_number = math.sqrt(number)
    toc()
    pass

def main():
    sqrt_number()
    

if "__name__" == main():
    main()