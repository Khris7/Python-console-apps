import random

def generate_question(level):
    if level == "easy":
        a, b = random.randint(1, 10), random.randint(1, 10)
    elif level == "medium":
        a, b = random.randint(10, 50), random.randint(10, 50)
    else:  # hard
        a, b = random.randint(50, 100), random.randint(1, 100)

    operation = random.choice(["+", "-", "*", "/"])

    if operation == "/":
        b = random.randint(1, 10)
        a = b * random.randint(1, 10)  # ensure a is divisible by b

    question = f"{a} {operation} {b}"
    answer = eval(question)

    if operation == "/":
        answer = round(answer, 2)
    else:
        answer = int(answer)

    return question, answer


def quiz():
    print("🎉 Welcome to the Math Quiz Game!")

    level = input("Choose difficulty (easy, medium, hard): ").lower()
    while level not in ("easy", "medium", "hard"):
        level = input("Invalid input. Choose difficulty (easy, medium, hard): ").lower()

    score = 0

    for i in range(5):
        question, correct_answer = generate_question(level)
        print(f"\nQuestion {i + 1}: {question} = ?")

        try:
            user_answer = float(input("Your answer: "))

            if isinstance(correct_answer, float):
                is_correct = abs(user_answer - correct_answer) < 0.01
            else:
                is_correct = user_answer == correct_answer

            if is_correct:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. The correct answer was {correct_answer:.2f}" 
                      if isinstance(correct_answer, float) else
                      f"❌ Incorrect. The correct answer was {correct_answer}")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    print(f"\n🏁 Quiz finished! Your score: {score}/5")


def main():
    while True:
        quiz()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()
