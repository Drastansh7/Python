def has_punctuation(string):
    punctuation = [".", "'", ",", ";", ":", "?", "!"]
    for i in string:
        if i in punctuation:
            return True
    return False