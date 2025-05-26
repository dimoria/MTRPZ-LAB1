import sys
import math
import os

def parse_input(value):
    try:
        return float(value)
    except ValueError:
        print(f"Error. Expected a valid real number, got {value} instead")
        return None

def solve_equation(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    if a == 0:
        print("Error. a cannot be 0")
        sys.exit(1)

    d = b**2 - 4*a*c
    if d < 0:
        print("There are 0 roots")
    elif d == 0:
        x = -b / (2*a)
        print("There are 1 roots")
        print(f"x1 = {x}")
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b - sqrt_d) / (2*a)
        x2 = (-b + sqrt_d) / (2*a)
        print("There are 2 roots")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

#Інтерактивний режим
def interactive_mode():
    while True:
        a = parse_input(input("a = "))
        if a is not None:
            break
    while True:
        b = parse_input(input("b = "))
        if b is not None:
            break
    while True:
        c = parse_input(input("c = "))
        if c is not None:
            break
    solve_equation(a, b, c)

#Неінтерактивний (файловий режим)
def file_mode(path):
    if not os.path.exists(path):
        print(f"file {path} does not exist")
        sys.exit(1)
    try:
        with open(path) as f:
            line = f.readline().strip()
            parts = line.split()
            if len(parts) != 3:
                raise ValueError
            a, b, c = map(float, parts)
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
            solve_equation(a, b, c)
    except Exception:
        print("invalid file format")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python equation.py [file]")