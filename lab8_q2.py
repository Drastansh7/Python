# drastansh nadola
# CS - UY 1121
# 30 March 2023 # Lab 8
# Problem No.: 2

def sums_and_products(**kwargs):

    values = list(kwargs.values())
    product = 1
    for value in values:
        product *= value
    return {
        'product': product,
        'sum': sum(values),
        'input': kwargs
    }


def main():
    test_cases = [
        ({'one': 1, 'two': 2, 'three': 3}, {'sum': 6, 'product': 6, 'input': {'one': 1, 'two': 2, 'three': 3}}),
        ({'four': 4, 'five': 5, 'six': 6, 'ten': 10, 'one': 1, 'fifteen': 15},
         {'product': 18000, 'sum': 41, 'input': {'four': 4, 'five': 5, 'six': 6, 'ten': 10, 'one': 1, 'fifteen': 15}}),
        ({}, {'product': 1, 'sum': 0, 'input': {}}),
        ({'a': 2, 'b': 3, 'c': 'abc'}, {'product': 6, 'sum': 5, 'input': {'a': 2, 'b': 3, 'c': 'abc'}}),
    ]
    for input_dict, expected_output in test_cases:
        actual_output = sums_and_products(**input_dict)
        assert actual_output == expected_output, f"Failed for {input_dict}. Expected {expected_output}, but got {actual_output}."


if __name__ == '__main__':
    main()


