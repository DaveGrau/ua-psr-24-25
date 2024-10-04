import cmath

def addComplex(x,y):
    added_complex = tuple(map(lambda i, j: i + j, x, y))
    printComplex(added_complex)
    return addComplex

def multiplyComplex(x,y):
    a,b = x
    c, d = y
    multiplied_complex = (a*c - b*d, a*d + c*d)
    return multiplyComplex

def printComplex(x):
    a, b = x
    """
    if b == 0:
        print(f"{a}")
    elif b > 0:
        print(f"{a} + {b}i")
    else:
        print(f"{a} - {-b}i")
    """
    print(f"{complex(a,b)}")
    pass
def main():
    x = (3,9)
    printComplex(x)
    y = (2,3)
    printComplex(y)
    
    addComplex(x,y)
    multiplyComplex(x,y)
    printComplex(x)

if "__name__" == main():
    main()