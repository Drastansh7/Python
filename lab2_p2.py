def int_extractor(*strings):
    integer_values = []
    for string in strings:
        words = string.split()
        for word in words:
            if word.isdigit():
                integer_values.append(word)
    return integer_values

print(int_extractor("Get only the numbers 1","in a sentence like 'In 1984","there were 13 instances of a","protest with over 1000 people attending' - 42"))