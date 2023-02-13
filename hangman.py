import random


def hangman(word):
    wrong = 0
    stages = ["",
              " ______          ",
              "|      |         ",
              "|      |         ",
              "|      O         ",
              "|     /|\        ",
              "|     / \        ",
              "|                "
              ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("HANGMAN GAME")


    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess letter: "
        char = input(msg)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0: wrong]))
        print("You have lost! You had to guess the word: {}.".format(word))



words_dict = {'animals': ['fox', 'elephant', 'snake', 'bear', 'dog', 'cat'],
              'nations': ['poland', 'spain', 'england', 'usa', 'france'],
              'capitals': ['warsaw', 'madryt', 'londyn', 'washington', 'paris'],
              'colors': ['blue', 'red', 'purple', 'green', 'orange', 'black'],
              'fruits': ['apple', 'peach', 'banana', 'pineapple', 'watermelon']
              }


while True:
    print("Category: {}".format(list(words_dict.keys())))
    category = input("Please choose category: ")
    if category in words_dict.keys():
        random_word = random.randint(0, len(words_dict[category]) - 1)
        word_choice = words_dict[category][random_word]
    else:
        print('There is no such category!')
        break

    hangman(word_choice)
    play_again = input("Do you want to play again? [y/n]: ")
    if play_again.lower() == 'y':
        continue
    else:
        break
