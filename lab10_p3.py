def recursive_length(string):
    if string == "":
        return 0
    else:
        return 1 + recursive_length(string[1:])