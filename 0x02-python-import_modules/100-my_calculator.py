#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    from calculator_1 import add, sub, mul, div
    import sys
    a = sys.argv[1]
    b = sys.argv[3]
    operator = sys.argv[2]

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Unknown operatorerator. Available operators: +, -, * and /")
