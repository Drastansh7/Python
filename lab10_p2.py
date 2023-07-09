def product_evens(n):
    if n == 2:
        return 2
    else:
        return n * product_evens(n-2)
