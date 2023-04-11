string_var = 'Hi,world'
print(string_var[::-1])
len_string = len(string_var)
list_string = list(string_var)
new_string = '|'.join(list_string[::3])


def string(n):
    dict1 = {}
    for i in n:
        dict1[i] = dict1.get(i, 0) + 1
    return dict1


def string1(n):
    str_set = set(n)
    dict1 = {}
    for i in str_set:
        dict1[i] = n.count(i)
    return dict1


def max_string(n):
    max_args = n[0]
    for i in range(1, len(n)):
        if len(n[i]) > len(max_args):
            max_args = n[i]
    return max_args


def divide_and_glue(string2, delimiter):
    s = sorted(string2.split(delimiter))
    return delimiter.join(s)


def string_list(n):
    print(''.join(map(str, n)))
