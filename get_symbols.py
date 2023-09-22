def symbols():
    file = open("symbols.txt", "r")

    word = file.read()

    file.close()

    return word
