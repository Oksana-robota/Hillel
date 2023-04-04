# 1
def max_out_of_two(a: (int, float), b: (int, float)):
    if a > b:
        return a
    return b


# 2
def min_out_of_thee(a: (int, float), b: (int, float), c: (int, float)):
    if a > c and b > c:
        return c
    elif a > b and c > b:
        return b
    return a


# 3
def number_abs(a: (int, float)):
    if a < 0:
        return a * -1
    return a


# 4
def values_sum(a, b):
    print(a + b)


# 5
def pos_or_neg_number(a: (int, float)):
    if a == 0:
        print('It is Zero')
    else:
        print(f'The number is {("positive", "negative")[a < 0]}')


