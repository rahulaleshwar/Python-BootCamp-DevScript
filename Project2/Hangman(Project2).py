import random

def word_for_guess():
    return random.choice(list_of_words).upper()

list_of_words = ['drill', 'waste', 'build', 'elbow', 'glove', 'sport', 'shock',
                 'cruel', 'black', 'state', 'grind', 'shake', 'donor', 'chaos',
                 'abbey', 'acute', 'chief', 'horse', 'bowel', 'tough', 'cable',
                 'brand', 'steak', 'enjoy', 'swipe', 'blade', 'space', 'arrow',
                 'owner', 'stain', 'weave', 'force', 'blame', 'coach', 'jelly',
                 'summit', 'dealer', 'string', 'pillow', 'couple', 'earwax', 'locate',
                 'assume', 'option', 'desire', 'decade', 'advice', 'senior', 'leader',
                 'timber', 'cheque', 'banner', 'treaty', 'credit', 'reduce', 'coffee',
                 'budget', 'system', 'embryo', 'charge', 'cheese', 'tender', 'mother',
                 'bubble', 'jacket', 'square', 'thrust', 'lounge', 'runner', 'switch',
                 'gift', 'code', 'core', 'wire', 'loss', 'slab', 'slam', 'sell', 'bell',
                 'sofa', 'bite', 'miss', 'cane', 'pull', 'knee', 'post', 'iron', 'herd',
                 'bind', 'even', 'area', 'pass', 'dine', 'calm', 'food', 'deck', 'safe',
                 'pray', 'echo', 'vain', 'shed', 'rank', 'pair', 'cute', 'fool', 'beef',
                 'lean', 'swim', 'well', 'menu', 'tune', 'slot', 'plot', 'knot', 'yard']

def hangman_game(word):
    find_word = "_ " * len(word)
    guessed = False
    guessed_words = []
    tries = 6
    guessed_letters = []
    print("\n\t\tHANGMAN GAME !!!\n")
    print("Let's start the game...")
    print("Good Luck !!!")
    print(Hangman_image(tries),"\n")
    print(find_word)
    while not guessed and tries > 0:
        print(f"\n{tries} tries left...")
        guess = input("Any Guess ?\n").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"\n{guess} is already guessed...")
                print(f"\nWrong Guess...!!!\n{guess} is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"\nRight Guess...!!!\n{guess} is in the word")
                guessed_letters.append(guess)
                word_list = find_word.split()
                index = [i for i, l in enumerate(word) if l == guess]
                for i in index:
                    word_list[i] = guess
                find_word = " ".join(word_list)
                if "_" not in find_word:
                    guessed = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                print(f"\n{guess} is already guessed...")
            elif guess != word:
                print(f"\nWrong Guess...!!!\n{guess} is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                find_word = word
        else:
            print("\nInvalid guess...!!!")
        print(Hangman_image(tries),"\n")
        print(find_word)
        
    if guessed:
        print("\nYou guessed the word\n\n\t\tYOU WON...!!!")
    else:
        print(f"\nNo more tries left...\nYou didn't find the word, the word was {word}...\n")

def Hangman_image(tries):
    hangman = {6:"\n\t|_ _ _ _\n\t|\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|",
               5:"\n\t|_ _ _ _\n\t|\t|\n\t|\t0\n\t|\n\t|\n\t|\n\t|\n\t|\n\t|",
               4:"\n\t|_ _ _ _\n\t|\t|\n\t|\t0\n\t|\t|\n\t|\t|\n\t|\n\t|\n\t|\n\t|",
               3:"\n\t|_ _ _ _\n\t|\t|\n\t|     \ 0 /\n\t|      \|/\n\t|\t|\n\t|\n\t|\n\t|\n\t|",
               2:"\n\t|_ _ _ _\n\t|\t|\n\t|     \ 0 /\n\t|      \|/\n\t|\t|\n\t|\t|\n\t|\t|\n\t|\n\t|",
               1:"\n\t|_ _ _ _\n\t|\t|\n\t|     \ 0 /\n\t|      \|/\n\t|\t|\n\t|\t|\n\t|\t|\n\t|      / \\\n\t|     /   \\",
               0:"\n\t|_ _ _ _\n\t|\t|\n\t|     \ 0 /\n\t|      \|/\n\t|\t|\n\t|\t|\n\t|\t|\n\t|      / \\\n\t|     /   \\"
              }
    return hangman[tries]

def play_game():
    repeat = "yes"
    while repeat == "yes":
        word = word_for_guess()
        hangman_game(word)
        repeat = input("\nDo you wish to play again? (yes/no)\n").lower()


play_game()