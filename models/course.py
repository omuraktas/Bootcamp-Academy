class Course:
    def __init__(self, code, name, level="beginner"):
        self.code = code
        self.name = name
        self.level = level
        self.lessons = []
        self.quiz_questions = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def add_question(self, question):
        self.quiz_questions.append(question)

    def get_category(self):
        return self.code[:3]

    def __len__(self):
        return len(self.lessons)

    def __str__(self):
        return f"{self.code} - {self.name} ({self.level})"
    

class Lesson:
    def __init__(self, code, title, duration):
        self.code = code
        self.title = title
        self.duration = duration
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Tamamlandı" if self.completed else "Tamamlanmadı"
        return f"{self.code} - {self.title} - {self.duration} dk - {status}"