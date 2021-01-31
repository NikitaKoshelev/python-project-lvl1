from random import randint, choice

condition = "What is the result of the expression?"
operators = ["+", "-", "*"]


def calculating(num_1, num_2, symbol):
    if symbol == "+":
        result = num_1 + num_2
    elif symbol == "-":
        result = num_1 - num_2
    elif symbol == "*":
        result = num_1 * num_2
    return result


def get_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 10)
    operator = choice(operators)
    question = "{} {} {}".format(
        num1, operator, num2)
    answer = str(calculating(num1, operator, num2))
    return question, answer
