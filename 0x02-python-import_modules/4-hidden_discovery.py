#!/usr/bin/python3
if __name__ == "__main__":  # el codi no se debe exe cuando se importa
    import hidden_4
    x = dir(hidden_4)
    for i in x:
        if x[:1] != "__":
            print("\n".join(x))

