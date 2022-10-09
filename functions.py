import random


def integer_generator(x, y):
    return random.randint(x, y)


def guess_number(x, y):
    my_input = int(input(f"Choose a number between {x} and {y}: "))
    if my_input == integer_generator(x, y):
        return True
    else:
        return False


def level_guessing(lives):

    for x in [2, 4, 9, 16]:
        while lives:
            if guess_number(1, x):
                if x < 16:
                    print("Correct, you leveled up!")
                else:
                    print("Correct, you WON!")
                break
            else:
                lives = lives - 1
                print(f'You have {lives} lives remaining')
        if not lives:
            print('game over')
            break


if __name__ == '__main__':
    level_guessing(lives=3)



