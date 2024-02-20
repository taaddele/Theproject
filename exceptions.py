
import sys
try:
    a = int(input("enter a number:"))
    b = int(input("enter a nubmer: "))
except ValueError:
    print("error: invalid input")
    sys.exit(1)
try:
    result = a/b
    print(result)
except ZeroDivisionError:
    print("error: you are tyring to divide number by zero")
    sys.exit(1)
