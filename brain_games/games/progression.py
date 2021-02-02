from random import randint

DESCRIPTION = "What number is missing in the progression?"

progression_length = 10


def generate_progression(start, diff, progression_length):
    finish = start + (progression_length * diff)
    progression = list(range(start, finish, diff))
    return progression


def get_answer():
    start = randint(1, 100)
    diff = randint(1, 10)
    hidden_number = randint(1, progression_length - 1)
    progression = generate_progression(start, diff, progression_length)
    answer = progression.pop(hidden_number)
    progression.insert(hidden_number, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)
