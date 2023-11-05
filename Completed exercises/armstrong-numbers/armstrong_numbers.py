import random, math


def is_armstrong_number(number):
    length = len(str(number))
    res = 0
    for num in str(number):
        res += (int(num) ** length)

    if res == number:
        print("True")
        return True
    else:
        print("False")
        return False


random_number = math.floor(random.randint(1, 9)) * math.floor(random.randint(1, 9))
# print(random_number)
is_armstrong_number(random_number)