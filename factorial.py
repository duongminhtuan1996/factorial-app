def factorial(value):
    if value == 1 or value == 0:
        return 1
    else:
        return value * factorial(value-1)

