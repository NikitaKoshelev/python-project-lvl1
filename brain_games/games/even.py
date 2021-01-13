from random import randint

print("Answer \"yes\" if the number is even, otherwise answer \"no\".")


def is_even(number):
    return number % 2 == 0


def get_answer():
    question = randint(0, 100)
    if is_even(question) is True:
        answer = "yes"
    else:
        answer = "no"
    return question, answer


print(is_even(101))
