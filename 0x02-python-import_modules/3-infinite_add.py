#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    import sys
    i = 1
    result = 0
    while i < len(sys.argv):
        result = result + int(sys.argv[i])
        i += 1
    print("{}".format(result))
