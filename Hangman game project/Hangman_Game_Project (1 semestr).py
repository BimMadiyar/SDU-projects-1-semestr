import random
import sys
words = ['program', 'amirkhan', 'hunter', 'sdudent', 'information', 'history', 'button', 'game', 'homework', 'python', 'wall', 'computer', 'minecraft', 'library',
         'window', 'capital', 'almaty', 'letter', 'building', 'laptop', 'qwerty', 'hangman', 'floor', 'ceiling', 'kitchen', 'output', 'engineer', 'teacher', 'arm'
         'introduction', 'java', 'door', 'slippers', 'bed', 'light', 'human', 'cat', 'dog', 'horse', 'sdu', 'pillow', 'pinduoduo', 'instagram', 'whatsapp', 'tiktok']
history = []
print('YOU ARE WELCOME TO THIS HANGMAN GAME!')
print()

def main_menu():
    print("THE MAIN MENU")
    print("1. Start")
    print("2. The history of the words")
    print("3. Introduction")
    print("4. End the Game")
    try:
        choose_button = int(input("Choose the number between (1 - 4): "))
        if choose_button > 4 or choose_button < 1:
            print("Please choose the number between (1 - 4)!")
            print()
            main_menu()
        elif choose_button == 3:
            print()
            introduction()
        elif choose_button == 1:
            print()
            start()
        elif choose_button == 2:
            print()
            history_words()
        elif choose_button == 4:
            print()
            sys.exit()
    except ValueError:
        print("Please choose the number, not string!")
        print()
        main_menu()

def introduction():
    print("INTRODUCTION")
    print("This is version of the classic letter guessing game called Hangman. "
          "You are shown a set of blank letters that match a word or phrase and "
          "you have to guess what these letters are to reveal the hidden word. "
          "You guess by picking letters from those displayed on the sides. If "
          "you pick a letter that is in the word, that letter "
          "is revealed from the blank letters; however, if you pick a letter that "
          "is not in the word, then your attempts will decreased by 1. "
          "This is why the game is called 'Hangman'. In this game you will have only 7 attempts."
          "If you can reveal all the letters in the word before attempts are over then "
          "you are successful and the full word is revealed along with an image showing "
          "the meaning of the word. The words can come out again(repeatedly).")
    print()
    main_menu()

def start():
    random_word = random.choice(words)
    history.append(random_word)
    lose_word = random_word
    random_word = list(random_word)
    hidden_word = []
    attempts = 7
    for i in range(len(random_word)):
        hidden_word.append('*')
    print("THE GAME IS STARTED!")
    print("The word is hidden:", ' '.join(hidden_word), "(attempts: 7)")
    guessed_letters = []
    while attempts != 0:
        guess_letter = input(f"Enter the letter in the word: {' '.join(hidden_word)} -> ")
        if len(guess_letter) >= 2:
            print("Please Enter only ONE letter!",  f"(attempts: {attempts})")
        elif guess_letter in random_word:
            if guess_letter not in guessed_letters:
                guessed_letters.append(guess_letter)
                for i in range(random_word.count(guess_letter)):
                    hidden_word[random_word.index(guess_letter)], random_word[random_word.index(guess_letter)] = guess_letter, '*'
            if '*' not in hidden_word:
                print()
                print("You are Winner! :) ")
                history.append('Win')
                print("THE HIDDEN WORD IS:", ''.join(hidden_word).capitalize())
                break
        elif guess_letter not in random_word:
            if guess_letter in guessed_letters:
                print("You already entered this letter, choose another letter!", f"(attempts: {attempts})")
            else:
                guessed_letters.append(guess_letter)
                attempts -= 1
                print(f"{guess_letter} is not in the word! (attempts: {attempts})")
    if attempts == 0:
        print()
        print("Unfortunately, you lose the Game :( ")
        history.append('Lose')
        print(f"THE HIDDEN WORD IS: {lose_word.capitalize()}")
    print()
    main_menu()

def history_words():
    if len(history) == 0:
        print("You haven't played a game yet!")
    else:
        for i in range(len(history)):
            if i % 2 == 0:
                print(history[i].capitalize(), "->", history[i + 1])
    print()
    main_menu()
main_menu()