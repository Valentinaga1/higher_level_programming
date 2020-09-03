#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    from add_0 import add
    a = 1  # se definen las var
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))  # llamo la funcion add
