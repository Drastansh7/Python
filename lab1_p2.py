def pete_and_dan(fraction):
    if fraction == "whole":
        grams = ounce_in_grams
    elif fraction == "half":
        grams = ounce_in_grams/2
    elif fraction == "fourth":
        grams = ounce_in_grams/4
    elif fraction == "eighth":
        grams = ounce_in_grams/8
    elif fraction == "sixteenth":
        grams = ounce_in_grams/16
    else:
        return "invalid fraction string"

    return "{:.2f} grams".format(grams)


