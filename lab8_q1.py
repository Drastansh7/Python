
# drastansh nadola
# CS - UY 1121
# 30 March 2023 # Lab 8
# Problem No.: 1

def count_digits(data_list):

    counts = {digit: 0 for digit in range(10)}  # initialize counts to 0 for all digits
    for number in data_list:
        if isinstance(number, int) and 0 <= number <= 9:
            counts[number] += 1
    return counts


def main():

    test_cases = [
        ([1, 2, 3, 'nyu'], {1: 1, 2: 1, 3: 1}),
        ([2, 0, 1, 9, 'nyu', 0, 12, 4, 1, 9], {2: 1, 0: 2, 1: 2, 9: 2, 4: 1}),
        ([], {digit: 0 for digit in range(10)}),
        ([11, 'a', None], {digit: 0 for digit in range(10)}),
    ]
    for data_list, expected_counts in test_cases:
        actual_counts = count_digits(data_list)
        assert actual_counts == expected_counts, f"Failed for {data_list}. Expected {expected_counts}, but got {actual_counts}."


if __name__ == '__main__':
    main()
