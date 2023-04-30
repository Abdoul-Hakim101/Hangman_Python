import random

list_words = ["python", "java", "swift", "javascript"]
random_word = random.choice(list_words)
hints = list("-" * len(random_word))
guessed_words = []
print("H A N G M A N")
win_loss = [0, 0]

def check_input(char):
    if len(char.strip()) != 1:
        print("Please, input a single letter.")
        return False
    elif not char.islower():
        print("Please, enter a lowercase letter from the English alphabet.")
        return False
    return True


def check_letter(char, guessed_):
    check = "not_found"
    if char in guessed_:
        # guessed_words = list(dict.fromkeys(guessed_words))
        print("You've already guessed this letter.")
        check = "guessed"
    else:
        for i in range(len(random_word)):
            if random_word[i] == char and hints[i] == "-":
                check = "move"
                hints[i] = char
    guessed_.append(char)
    return check


def game(win):
    lost = True
    counter = 0
    while counter < 8:
        print("\n" + "".join(hints))
        character = input("Input a letter: ")
        if check_input(character):
            x = check_letter(character, guessed_words)
            if x == "not_found":
                print("That letter doesn't appear in the word.")
                counter += 1
        if "".join(hints) == random_word:
            lost = False
            print(f"""\nYou guessed the word {random_word}!
You survived!""")
            win[0] = win[0] + 1
            counter = 8
    if lost:
        print("You lost!")
        win[1] += 1


while True:

    type_ = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if type_ == "play":
        hints = list("-" * len(random_word))
        guessed_words = []
        game(win_loss)
    elif type_ == "exit":
        exit(0)
    elif type_ == "results":
        print(f"""You won: {win_loss[0]} times.
You lost: {win_loss[1]} times.""")
