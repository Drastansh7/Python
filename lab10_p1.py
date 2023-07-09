def sum_of(n):
    if n == 0:
        return 0
    else:
        return n + sum_of(n-1)
