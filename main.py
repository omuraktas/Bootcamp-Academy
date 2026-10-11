from models.user import Student, Instructor, Admin
from models.course import Course, Lesson
from models.quiz import Question, Quiz
from utils.input_helper import get_int_input
from services.calculator import calculate_success_rate, calculate_level


users = [
    Student("ali", "1234"),
    Student("ayse", "1234"),
    Instructor("mehmet", "1234"),
    Admin("admin", "admin")
]


python_course = Course("PYT-101", "Python Temelleri", "beginner")

python_course.add_lesson(Lesson("L001", "Değişkenler", 15))
python_course.add_lesson(Lesson("L002", "String İşlemleri", 20))
python_course.add_lesson(Lesson("L003", "Listeler", 25))
python_course.add_lesson(Lesson("L004", "Sözlükler", 20))
python_course.add_lesson(Lesson("L005", "Fonksiyonlar", 30))


q1 = Question(
    "Python'da liste hangi sembol ile oluşturulur?",
    {"a": "()", "b": "[]", "c": "{}"},
    "b"
)

q2 = Question(
    "Dictionary hangi yapıdadır?",
    {"a": "key-value", "b": "sadece sayı", "c": "sadece string"},
    "a"
)

q3 = Question(
    "Bir sınıftan nesne üretmeye ne denir?",
    {"a": "loop", "b": "instance", "c": "slice"},
    "b"
)


python_course.add_question(q1)
python_course.add_question(q2)
python_course.add_question(q3)


courses = {
    python_course.code: python_course
}


def login():
    username = input("Kullanıcı adı: ").lower().strip()
    password = input("Şifre: ").strip()

    for user in users:
        if user.username == username and user.check_password(password):
            print(f"Giriş başarılı. Hoş geldin {user.username}")
            return user
        else:
            print("Kullanıcı adı veya şifre hatalı.")
            return None


def show_courses():
    print("\nKurs Listesi")

    for code, course in courses.items():
        print(course)
        print(f"Ders sayısı: {len(course)}")
        print("-" * 30)


def check_badges(student):
    if student.score >= 50:
        student.add_badge("Başlangıç Rozeti")

    if student.score >= 150:
        student.add_badge("Çalışkan Öğrenci Rozeti")

    if student.score >= 300:
        student.add_badge("Python Uzmanı Rozeti")


def student_menu(student):
    while True:
        student.show_panel()
        choice = get_int_input("Seçiminiz: ")

        if choice == 1:
            show_courses()

        elif choice == 2:
            show_courses()
            code = input("Kayıt olmak istediğiniz kurs kodu: ").upper().strip()

            if code in courses:
                student.enroll_course(code)
            else:
                print("Böyle bir kurs yok.")

        elif choice == 3:
            if len(student.enrolled_courses) == 0:
                print("Önce bir kursa kayıt olmalısınız.")
                continue

            print("\nKayıtlı olduğunuz kurslardaki dersler:")

            for course_code in student.enrolled_courses:
                course = courses[course_code]

                print(f"\n{course.name} dersleri:")
                for lesson in course.lessons:
                    print(lesson)

            lesson_code = input("Tamamlamak istediğiniz ders kodu: ").upper().strip()

            found = False

            for course_code in student.enrolled_courses:
                course = courses[course_code]

                for lesson in course.lessons:
                    if lesson.code == lesson_code:
                        student.complete_lesson(lesson_code)
                        lesson.complete()
                        check_badges(student)
                        found = True
                        break

                if found:
                    break

            if not found:
                print("Ders bulunamadı.")

        elif choice == 4:
            if len(student.enrolled_courses) == 0:
                print("Önce kursa kayıt olmalısınız.")
                continue

            for course_code in student.enrolled_courses:
                course = courses[course_code]

                if len(course.quiz_questions) == 0:
                    print("Bu kursta quiz yok.")
                    continue

                quiz = Quiz(course.quiz_questions)
                quiz_score = quiz.start()
                student.score += quiz_score

                print(f"Quiz puanınız: {quiz_score}")

                if quiz_score >= 20:
                    student.add_badge("Quiz Başarılı")

                check_badges(student)

        elif choice == 5:
            print("\nProfil")
            print(f"Kullanıcı: {student.username}")
            print(f"Puan: {student.score}")
            print(f"Seviye: {calculate_level(student.score)}")
            print(f"Kayıtlı kurslar: {student.enrolled_courses}")
            print(f"Tamamlanan dersler: {student.completed_lessons}")
            print(f"Rozetler: {student.badges}")

            total_lessons = 0

            for course_code in student.enrolled_courses:
                total_lessons += len(courses[course_code].lessons)

            rate = calculate_success_rate(
                len(student.completed_lessons),
                total_lessons
            )

            print(f"Başarı oranı: %{rate:.2f}")

        elif choice == 0:
            print("Öğrenci panelinden çıkılıyor.")
            break

        else:
            print("Geçersiz seçim.")


def instructor_menu(instructor):
    while True:
        instructor.show_panel()
        choice = get_int_input("Seçiminiz: ")

        if choice == 1:
            show_courses()

        elif choice == 2:
            show_courses()
            course_code = input("Ders eklenecek kurs kodu: ").upper().strip()

            if course_code not in courses:
                print("Kurs bulunamadı.")
                continue

            lesson_code = input("Ders kodu: ").upper().strip()
            lesson_title = input("Ders başlığı: ").strip()
            duration = get_int_input("Ders süresi dakika: ")

            new_lesson = Lesson(lesson_code, lesson_title, duration)
            courses[course_code].add_lesson(new_lesson)

            print("Ders başarıyla eklendi.")

        elif choice == 3:
            show_courses()
            course_code = input("Quiz sorusu eklenecek kurs kodu: ").upper().strip()

            if course_code not in courses:
                print("Kurs bulunamadı.")
                continue

            text = input("Soru metni: ")

            options = {}
            options["a"] = input("A şıkkı: ")
            options["b"] = input("B şıkkı: ")
            options["c"] = input("C şıkkı: ")

            correct_answer = input("Doğru cevap: ").lower().strip()

            if correct_answer not in ["a", "b", "c"]:
                print("Cevap sadece a, b veya c olabilir.")
                continue

            new_question = Question(text, options, correct_answer)
            courses[course_code].add_question(new_question)

            print("Quiz sorusu eklendi.")

        elif choice == 0:
            print("Eğitmen panelinden çıkılıyor.")
            break

        else:
            print("Geçersiz seçim.")


def admin_menu(admin):
    while True:
        admin.show_panel()
        choice = get_int_input("Seçiminiz: ")

        if choice == 1:
            print("\nKullanıcılar")

            for user in users:
                print(user)

        elif choice == 2:
            show_courses()

        elif choice == 3:
            total_students = 0
            total_instructors = 0
            total_admins = 0

            for user in users:
                if user.role == "student":
                    total_students += 1
                elif user.role == "instructor":
                    total_instructors += 1
                elif user.role == "admin":
                    total_admins += 1

            total_lessons = 0
            total_questions = 0

            for course in courses.values():
                total_lessons += len(course.lessons)
                total_questions += len(course.quiz_questions)

            print("\nSistem İstatistikleri")
            print(f"Öğrenci sayısı: {total_students}")
            print(f"Eğitmen sayısı: {total_instructors}")
            print(f"Admin sayısı: {total_admins}")
            print(f"Kurs sayısı: {len(courses)}")
            print(f"Toplam ders sayısı: {total_lessons}")
            print(f"Toplam quiz sorusu: {total_questions}")

        elif choice == 0:
            print("Admin panelinden çıkılıyor.")
            break

        else:
            print("Geçersiz seçim.")


def main():
    while True:
        print("""
BOOTCAMP AKADEMİ SİSTEMİ

1. Giriş Yap
0. Çıkış
""")

        choice = get_int_input("Seçiminiz: ")

        if choice == 1:
            current_user = login()

            if current_user is None:
                continue

            if current_user.role == "student":
                student_menu(current_user)

            elif current_user.role == "instructor":
                instructor_menu(current_user)

            elif current_user.role == "admin":
                admin_menu(current_user)

        elif choice == 0:
            print("Program kapatılıyor.")
            break

        else:
            print("Geçersiz seçim.")


main()