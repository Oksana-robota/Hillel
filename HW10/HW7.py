import random


# 1
def retry(attempts=5, desired_value=None):
    for _ in range(attempts):
        def wrapper(func):
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                if result == desired_value:
                    return result
                else:
                    print('There is no result')

            return inner

        return wrapper


######### examples of implemented 'retry' decorator
@retry(desired_value=3)
def get_random_value_with_default_attempts():
    return random.choice((1, 2, 3, 4, 5))


@retry(desired_value=[1, 2])
def get_random_values_with_default_attempts(choices, size=2):
    return random.choices(choices, k=size)


@retry(attempts=7, desired_value=3)
def get_random_value():
    return random.choice((1, 2, 3, 4, 5))


@retry(attempts=2, desired_value=[1, 2, 3])
def get_random_values(choices, size=2):
    return random.choices(choices, k=size)


# 2
def copy_file(path_from, path_to):
    file1 = open(path_from)
    text = file1.read()
    file2 = open(path_to, 'w')
    file2.write(text)
    file1.close()
    return file2.close()


# 3
def read_big_file(path):
    file = open(path)
    dict_top = {}
    rows = 0
    bite_size = 0
    while True:
        line = file.readline()
        if not line:
            break
        else:
            bite_size += len(line.encode('utf-8'))
            line1 = line.replace(' ', '').rstrip()
            for i in line1:
                dict_top[i] = dict_top.setdefault(i, 0) + 1
            rows += 1
    top_3 = {i[0]: i[1] for i in sorted(dict_top.items(), key=lambda x: -x[1])[:3]}
    return {'amount_of_rows': rows, 'bite_size': bite_size, 'top_3': top_3}
