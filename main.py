class School:
    def __init__(self):
        self.teachers = []
        self.subjects = []
        self.schedules = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_schedule(self, teacher, subject, time):
        self.schedules.append({"teacher": teacher, "subject": subject, "time": time})

class Teacher:
    def __init__(self, name):
        self.name = name

class Subject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Schedule:
    def __init__(self, teacher, subject, time):
        self.teacher = teacher
        self.subject = subject
        self.time = time

    def __str__(self):
        return f"{self.teacher.name} - {self.subject.name} - {self.time}"

school = School()
teacher1 = Teacher("John")
teacher2 = Teacher("Mike")
subject1 = Subject("Math")
subject2 = Subject("Science")
school.add_teacher(teacher1)
school.add_teacher(teacher2)
school.add_subject(subject1)
school.add_subject(subject2)
school.add_schedule(teacher1, subject1, "10:00")
school.add_schedule(teacher2, subject2, "11:00")
for schedule in school.schedules:
    print(schedule["teacher"].name, schedule["subject"].name, schedule["time"])