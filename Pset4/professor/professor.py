
import random
import sys

def main():
    level = get_level()
    question_list = []

    score = 0
    number_of_questions = 10
    for question in range(number_of_questions):
        question_list.append(generate_question(level))

    for question in question_list:
        print(question[0])

        chances = 3
        while chances > 0:
            try:
                answer = int(input("Your answer is...? "))
                if answer != question[1]:
                    print("EEE")
                    chances -= 1
                else:
                    print("Correct!")
                    score += 1
                    break
            except ValueError:
                print("Input a number")
            except EOFError:
                sys.exit("Why leaving so soon?")

    print()
    print("SCORE =", score)

def get_level():
    while True:
        try:
            n = int(input("Input a level between 1 and 3: "))
            if n in [1,2,3]:
                break
        except ValueError:
            print("Must be an integer")

    return n

def generate_integer(level):
    max_number = int('9' * level)
    return random.randint(0, max_number)

def generate_question(level):
    gen_x = generate_integer(level)
    gen_y = generate_integer(level)

    result = gen_x + gen_y
    return f'{gen_x} + {gen_y} = ',result

if __name__ == "__main__":
    main()