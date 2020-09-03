#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    import hidden_4
    x = dir(hidden_4)
    for i in x:
        if i[:1] != "_":
            print("".join(i))
