import random

print('H A N G M A N\n')

def main():
    while True:
        print("Type 'play' to play the game, 'exit' to quit: ")
        action = input()

        if action == "play":
            words = ['python', 'java', 'kotlin', 'javascript']
            target_word = random.choice(words)
            masked_word = "-" * len(target_word)
            tried_letters = list()
            remaining_attempts = 8

            print("Chosen word:", target_word)  # debug

            while (remaining_attempts > 0) and (masked_word != target_word):
                print("Remaining attempts:", remaining_attempts)
                print("Current progress:", masked_word)
                tried_letter = input("Input a letter: ")

                if tried_letter in tried_letters:
                    remaining_attempts -= 1
                    print("No improvements")

                elif tried_letter in target_word:
                    tried_letters.append(tried_letter)
                    masked_word = "".join("-" if (target_letter not in tried_letters)
                                          else target_letter
                                          for target_letter in target_word)
                    print("Good guess !")

                elif tried_letter not in target_word:
                    tried_letters.append(tried_letter)
                    remaining_attempts -= 1
                    print("That letter doesn't appear in the word")

                print()

            if remaining_attempts == 0:
                print("You lost!")
            elif target_word == masked_word:
                print(target_word)
                print("You guessed the word!")
                print("You survived!")

            print('''
            Thanks for playing!
            We'll see how well you did in the next stage
            ''')
        elif action == "exit":
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()