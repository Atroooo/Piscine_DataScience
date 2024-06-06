from new_student import Student


student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward")
    print(student)
except Exception as e:
    print(e)

try:
    student = Student(surname="agle")
    print(student)
except Exception as e:
    print(e)

try:
    student = Student(name=1, surname="agle")
    print(student)
except Exception as e:
    print(e)

try:
    student = Student(name="Edward", surname=1)
    print(student)
except Exception as e:
    print(e)

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except Exception as e:
    print(e)
