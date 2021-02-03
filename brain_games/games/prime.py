from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


def get_answer():
    question = randint(1, 100)
    if is_prime(question) is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
