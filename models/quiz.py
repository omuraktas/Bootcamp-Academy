import random

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def ask(self):
        print(self.text)

        for key, value in self.options.items():
            print(f"{key}) {value}")

        answer = input("Cevabınız: ").lower().strip()

        if answer == self.correct_answer:
            print("Doğru cevap!")
            return True
        else:
            print(f"Yanlış cevap. Doğru cevap: {self.correct_answer}")
            return False


class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def start(self, question_count=3):
        score = 0

        selected_questions = random.sample(
            self.questions,
            min(question_count, len(self.questions))
        )

        for question in selected_questions:
            result = question.ask()

            if result:
                score += 10

        return score