class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher Name: {self.name}, Subject: {self.subject}")

class Subject:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Subject Name: {self.name}")

class Schedule:
    def __init__(self, teacher, subject, day, time):
        self.teacher = teacher
        self.subject = subject
        self.day = day
        self.time = time

    def display_info(self):
        print(f"Day: {self.day}, Time: {self.time}, Teacher: {self.teacher.name}, Subject: {self.subject.name}")

class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.subjects = []
        self.schedules = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def display_schedules(self):
        for schedule in self.schedules:
            schedule.display_info()

school = School("ABC School")
math_teacher = Teacher("John", "Math")
english_teacher = Teacher("Jane", "English")
math_subject = Subject("Mathematics")
english_subject = Subject("English Language")

school.add_teacher(math_teacher)
school.add_teacher(english_teacher)
school.add_subject(math_subject)
school.add_subject(english_subject)

schedule1 = Schedule(math_teacher, math_subject, "Monday", "9:00 AM")
schedule2 = Schedule(english_teacher, english_subject, "Monday", "10:00 AM")
schedule3 = Schedule(math_teacher, math_subject, "Tuesday", "9:00 AM")
schedule4 = Schedule(english_teacher, english_subject, "Tuesday", "10:00 AM")

school.add_schedule(schedule1)
school.add_schedule(schedule2)
school.add_schedule(schedule3)
school.add_schedule(schedule4)

school.display_schedules()
math_teacher.display_info()
english_teacher.display_info()
math_subject.display_name()
english_subject.display_name()