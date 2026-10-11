class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = role

    def check_password(self, password):
        return self.password == password

    def show_panel(self):
        print("Genel kullanıcı paneli")

    def __str__(self):
        return f"{self.username} - {self.role}"


class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password, "student")
        self.enrolled_courses = set()
        self.completed_lessons = []
        self.score = 0
        self.badges = set()

    def enroll_course(self, course_code):
        self.enrolled_courses.add(course_code)
        print(f"{course_code} kursuna kayıt olundu.")

    def complete_lesson(self, lesson_code):
        if lesson_code not in self.completed_lessons:
            self.completed_lessons.append(lesson_code)
            self.score += 10
            print("Ders tamamlandı. +10 puan")
        else:
            print("Bu ders zaten tamamlanmış.")

    def add_badge(self, badge):
        self.badges.add(badge)

    def show_panel(self):
        print("""
Öğrenci Paneli
1. Kursları Gör
2. Kursa Kayıt Ol
3. Ders Tamamla
4. Quiz Çöz
5. Profilimi Gör
0. Çıkış
""")


class Instructor(User):
    def __init__(self, username, password):
        super().__init__(username, password, "instructor")

    def show_panel(self):
        print("""
Eğitmen Paneli
1. Kursları Gör
2. Derse İçerik Ekle
3. Quiz Sorusu Ekle
0. Çıkış
""")


class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password, "admin")

    def show_panel(self):
        print("""
Admin Paneli
1. Kullanıcıları Gör
2. Kursları Gör
3. Sistem İstatistikleri
0. Çıkış
""")