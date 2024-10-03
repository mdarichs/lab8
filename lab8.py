#Словник для збереження інформації про студентів
students_performance = {
    "Марюха Дар'я Анатоліївна": {
        'group_number': "КН-32",
        'course': 2,
        'subjects': {
            "ММДО": 96,
            "Алгоритми": 90,
            "Чисельні методи": 80
        }
    },
    "Єльнікова Анна Олексіївна": {
        'group_number': "КН-22",
        'course': 3,
        'subjects': {
            "ММДО": 61,
            "Алгоритми": 61,
            "Чисельні методи": 61
        }
    },
    "Половинка Софія Віталіївна": {
        'group_number': "КН-42",
        'course': 1,
        'subjects': {
            "ММДО": 79,
            "Алгоритми": 93,
            "Чисельні методи": 89
        }
    },
    "Кислий Олександр Романович": {
        'group_number': "КН-31",
        'course': 2,
        'subjects': {
            "ММДО": 68,
            "Алгоритми": 82,
            "Чисельні методи": 61
        }
    }
}

# Виведення кожного студента окремо
for student, details in students_performance.items():
    print(f"Студент: {student}")
    print(f"  Група: {details['group_number']}")
    print(f"  Курс: {details['course']}")
    print("  Предмети:")
    for subject, score in details['subjects'].items():
        print(f"    {subject}: {score}")
    print()  #Для відступу між студентами


#Марюха Дар'я
#Функція для додавання нового студента
def add_student():
    #Отримання інформації від користувача
    full_name = input("Введіть повне ім'я студента: ")
    group_number = input("Введіть номер групи: ")
    course = int(input("Введіть курс: "))

    #Отримуємо оцінки за предмети (максимум 3)
    subjects_grades = {}
    subject_count = 0
    while subject_count < 3:
        subject = input("Введіть назву предмета (або натисніть Enter для завершення): ")
        if subject == "":
            break
        grade = int(input(f"Введіть оцінку за предмет {subject}: "))
        subjects_grades[subject] = grade
        subject_count += 1
        if subject_count == 3:
            print("Досягнуто максимальної кількості предметів.")

    #Додаємо нового студента до словника
    students_performance[full_name] = {
        'group_number': group_number,
        'course': course,
        'subjects': subjects_grades
    }

#Виклик функції для додавання студента
add_student()

for student, details in students_performance.items():
    print(f"Студент: {student}")
    print(f"  Група: {details['group_number']}")
    print(f"  Курс: {details['course']}")
    print("  Предмети:")
    for subject, score in details['subjects'].items():
        print(f"    {subject}: {score}")
    print()  #Для відступу між студентами

 #Кислий Олександр
#Функція пошуку студентів за номером курсу
def get_older_students(students_performance):
    course_number = int(input("Введіть номер шуканого курсу: "))
    older_courses = []
    for student, details in students_performance.items():
        if details['course'] == course_number:
            older_courses.append((student, details['group_number'], details['subjects']))
    if older_courses:
        print("Студенти на курсі", course_number)
        for student in older_courses:
            print(f"Студент: {student[0]}")
            print(f"Група: {student[1]}")
            print("Предмети:")
            for subject, score in student[2].items():
                print(f"    {subject}: {score}")
    else:
        print(f"Немає студентів на курсі {course_number}")

#Виклик функції для додавання студента
add_student()
older_students=get_older_students(students_performance)

#Вивести словник для перевірки доданого студента
print(students_performance)
