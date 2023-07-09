def calc(string):
    list = string.split(' ')
    operand1 = int(list[0])
    operator = list[1]
    operand2 = int(list[2])
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2

    elif operator == '*':
        return operand1 * operand2

    else:
        return 'Invalid Operator'
