from random import randint

DESCRIPTION = "Find the greatest common divisor of given numbers"


def get_gdc(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def get_answer():
    number1 = randint(1, 55)
    number2 = randint(1, 55)
    question = "{} {}".format(number1, number2)
    answer = get_gdc(number1, number2)
    return question, str(answer)
