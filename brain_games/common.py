import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.RULE)
    for count in range(3):
        question, correct_answer = game.get_question_and_answer()
        print(question)
        user_answer = prompt.string("Your answer: ")
        if correct_answer != user_answer:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break
        else:
            print('Correct!')
            count += 1
    else:
        print(f'Congratulations, {name}!')
