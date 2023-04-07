# 1
def unique_values(*args: (float, int, bool, str, tuple)):
    res = [args[0]]
    for i in args[1:]:
        if i not in res:
            res += [i]
    return res


# 2
def kwarg_function(user_type='Student', **kwargs):
    kwargs.update({'user_type': user_type})
    len_dict = 0
    for _ in kwargs.values():
        len_dict += 1
    print(f'The lentgh is {len_dict}.', f'User type values is {user_type}.', sep='\n')


# 3
def arg_types(pos_1, pos_2, arg_3, imen_1, imen_2=3, imen_3=3):
    pass


# 4
def func(a: (int, float)):
    def func_in_func(b: (int, float)):
        return a * b

    return func_in_func


res = func(5)
print(res(6))


# 5
def recurs_square(len_sq: int, stop_arg=1):
    row = '*' * len_sq
    print(row)
    if stop_arg == len_sq:
        return row
    return recurs_square(len_sq, stop_arg + 1)
