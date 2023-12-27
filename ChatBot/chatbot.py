import random


def main():
    # Етап 1
    print("Hello! My name is DICT_Bot.")
    print("I was created in 2023.")

    # Етап 2
    name = input("Please, remind me your name.\n> ")
    print(f"What a great name you have, {name}!")

    # Етап 3
    remainder3 = int(input("Enter remainder of dividing your age by 3.\n> "))
    remainder5 = int(input("Enter remainder of dividing your age by 5.\n> "))
    remainder7 = int(input("Enter remainder of dividing your age by 7.\n> "))
    age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

    # Етап 4
    num = int(input("Now I will prove to you that I can count to any number you want.\n> "))
    for i in range(num):
        print(f"{i} !")
    print("Completed, have a nice day!")

    # Етап 5
    test_question = "Why do we use methods?"
    test_answers = ["To repeat a statement multiple times",
                    "To decompose a program into several small subroutines",
                    "To determine the execution time of a program",
                    "To interrupt the execution of a program"]
    correct_answer = random.choice(test_answers)
    while True:
        print(
            f"{test_question}?\n1. {test_answers[0]}\n2. {test_answers[1]}\n3. {test_answers[2]}\n4. {test_answers[3]}")
        answer = int(input("> "))
        if answer == correct_answer:
            print("Congratulations, have a nice day!")
            break
        else:
            print("Please, try again.")

if __name__ == "__main__":
    main()