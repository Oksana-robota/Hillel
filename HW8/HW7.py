import random
import string
import time


PASSWORD = ''.join(random.choices(string.ascii_letters, k=4))


def password_checker(password):
    for real_pass_char, passed_pass_char in zip(PASSWORD, password):
        if real_pass_char != passed_pass_char:
            return

        time.sleep(0.1)


# 1
def sum_of_list_items(arr):
    if len(arr) == 0:
        return 0
    if isinstance(arr[0], int):
        return arr[0] + sum_of_list_items(arr[1:])
    return sum_of_list_items(arr[0]) + sum_of_list_items(arr[1:])


# 2
def cycle_words(words, output_length):
    amount = output_length // len(words)
    amount1 = output_length % len(words)
    return (words * amount) + words[:amount1]


# 3
def password_cracker():
    letters = string.ascii_letters
    for letter1 in letters:
        start1 = time.time()
        password_checker(letter1)
        end1 = time.time()
        if (end1 - start1) >= 0.1:
            for letter2 in letters:
                start2 = time.time()
                password_checker(letter1+letter2)
                end2 = time.time()
                if (end2 - start2) >= 0.2:
                    for letter3 in letters:
                        start3 = time.time()
                        password_checker(letter1 + letter2 + letter3)
                        end3 = time.time()
                        if (end3 - start3) >= 0.3:
                            for letter4 in letters:
                                start4 = time.time()
                                password_checker(letter1 + letter2 + letter3 + letter4)
                                end4 = time.time()
                                if (end4 - start4) >= 0.4:
                                    return letter1 + letter2 + letter3 + letter4





