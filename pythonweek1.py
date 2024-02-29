print("welcome to codeworld")
name=input("Enter your name :")
age=input("Enter your age  :")
print("----------------------")
print("Hello",name,",you may start your quiz now")
class Quiz:
    def __init__(self, questions, options, answers):
        self.questions = questions
        self.options = options
        self.answers = answers
        self.guesses = []
        self.score = 0
        self.question_num = 0

    def start_quiz(self):
        for question in self.questions:
            print("----------------------")
            print(question)
            for option in self.options[self.question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()
            self.guesses.append(guess)
            self.evaluate_answer(guess)
            self.question_num += 1

        self.show_results()

    def evaluate_answer(self, guess):
        if guess == self.answers[self.question_num]:
            self.score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{self.answers[self.question_num]} is the correct answer")

    def show_results(self):
        print("----------------------")
        print(" RESULTS ")
        print("----------------------")

        print("answers: ", end="")
        for answer in self.answers:
            print(answer, end=" ")
        print()

        print("guesses: ", end="")
        for guess in self.guesses:
            print(guess, end=" ")
        print()

        self.score = int(self.score / len(self.questions) * 100)
        print(f"Your score is: {self.score}%")


def main():
    questions = (
        "what is 2*3 ?: ",
        " Which collection is ordered, changeable, and allows duplicate members?:",
        "Which collection does not allow duplicate members? : ",
        " Which statement is used to stop a loop?: ",
        "Which method can be used to return a string in upper case letters?: "
    )

    options = (
        ("A. 4", "B. 2", "C. 6", "D. 8"),
        ("A. dictionaries", "B. sets", "C. tuple", "D. list"),
        ("A. sets", "B. dictionaries", "C. tuple", "D. list"),
        ("A. break", "B. stop", "C. end", "D. print"),
        ("A. isupper()", "B. upper()", "C. islower()", "D. lower()")
    )

    answers = ("C", "D", "A", "A", "B")

    quiz = Quiz(questions, options, answers)
    quiz.start_quiz()


if __name__ == "__main__":
    main()
