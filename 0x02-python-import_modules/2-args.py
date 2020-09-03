#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("{} {}".format((len(sys.argv) - 1), "argument:"))
        print("{}{}".format("1: ", sys.argv[1]))
    else:
        print("{} {}".format((len(sys.argv) - 1), "arguments:"))
        i = 1
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
