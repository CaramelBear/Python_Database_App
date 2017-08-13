from peewee import *


db = MySQLDatabase('dev', user='root',password='kjoshi31')

class Student(Model):
    username = CharField(max_length=255, unique = True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {'username':'karanjoshi','points':31},
    {'username':'swaggyp','points':3},
    {'username':'charles','points':69},
    {'username':'hombre','points':54},
    {'username':'richard','points':21},
    {'username':'21Savage','points':211},
    {'username':'muchacho','points':78}
]


def add_students():
    for student in students:
        try:
            Student.create(username = student['username'],
                            points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']

            if student_record.points != student['points']:
                student_record.save(points = student['points']).where(username=student['username'])

            student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student],safe=True)
    add_students()
    print("Top Student right now is: {0.username}".format(top_student()))
