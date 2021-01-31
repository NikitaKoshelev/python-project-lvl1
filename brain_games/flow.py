import prompt

ROUNDS_COUNT = 3


def flow_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    print(game.DESCRIPTION)
    for i in range(ROUNDS_COUNT):
        question, correct_answer = game.get_answer()
        print("Question: {}".format(question))
        user_answer = prompt.string("Your answer: ")
        if correct_answer == user_answer:
            print("Correct!")
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, correct_answer
                )
            )
            print("Let`s try again, {}!".format(name))
            return
        print("Congratulations, {}!".format(name))
