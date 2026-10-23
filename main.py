
import random
import string
from collections import Counter

MAX_ATTEMPTS = 7
MAX_SCORE = 100
PENALTY = 10


def play_game():
    best_score = 0

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0
        score = MAX_SCORE

        print("\n--- Number Guessing Game ---")
        print("Guess a number between 1 and 100.")
        print(f"You have {MAX_ATTEMPTS} attempts.")

        while attempts < MAX_ATTEMPTS:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a whole number.")
                continue

            if not 1 <= guess <= 100:
                print("Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                print("Correct! You won!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            score = max(0, MAX_SCORE - attempts * PENALTY)
            print("Attempts used:", attempts)

        else:
            print("Out of attempts!")
            print("The secret number was:", secret_number)
            score = 0

        if attempts < MAX_ATTEMPTS and guess == secret_number:
            score = max(0, MAX_SCORE - (attempts - 1) * PENALTY)

        best_score = max(best_score, score)
        print("Your score:", score)
        print("Best score this session:", best_score)

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


def count_words(path="sample.txt"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()
    counts = Counter(words)

    print("\n--- Word Counter Results ---")
    print("Total words:", len(words))
    print("Unique words:", len(counts))

    if not counts:
        print("The file is empty.")
        return

    print("\nTop 10 most common words:")
    print(f"{'Word':<15}{'Count':>5}")
    print("-" * 20)

    for word, count in counts.most_common(10):
        print(f"{word:<15}{count:>5}")


def main():
    while True:
        print("\n===== PROJECT 02 =====")
        print("1. Play Number Guessing Game")
        print("2. Count Words in a File")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            count_words()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Select 1, 2, or 3.")


if __name__ == "__main__":
    main()
