def multiply(x, y):
    accumulator = 0
    for _ in range(y):
        accumulator = accumulator + x
    return accumulator
        

def exponent(x, y):
    accumulator = 1
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator

def square(x):
    return exponent(x, 2)

def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = multiply(x, y)
    print(result)
    result = exponent(x, y)
    print(result)
    result = square(x)
    print(result)

main()
