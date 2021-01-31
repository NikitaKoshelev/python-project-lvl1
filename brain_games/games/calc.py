from random import randint, choice

DESCRIPTION = "What is the result of the expression?"
operators = ["+", "-", "*"]


def calculating(num1, symbol, num2):
    if symbol == "+":
        result = num1 + num2
    elif symbol == "-":
        result = num1 - num2
    elif symbol == "*":
        result = num1 * num2
    return result


def get_answer():
    number1 = randint(1, 100)
    number2 = randint(1, 10)
    operator = choice(operators)
    question = "{} {} {}".format(
        number1, operator, number2)
    answer = str(calculating(number1, operator, number2))
    return question, answer
