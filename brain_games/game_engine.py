import prompt


ROUNDS_COUNT = 3


def run(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
