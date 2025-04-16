AFFIRMATION : str = "Main har mushkil ka samna kar sakta hoon."

def main():
    print(f"Please type the following affirmation: {AFFIRMATION.lower()}")

    user_feedback = input()
    while user_feedback.lower() != AFFIRMATION.lower():
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print(f"Please type the following affirmation: {AFFIRMATION}")
        user_feedback = input()

    print("That's right! :)")


if __name__ == '__main__':
    main()