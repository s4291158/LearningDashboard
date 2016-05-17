import random

from .models import *


def create_data_set(count=100):
    print("creating...")
    try:
        max_id = int(Student.objects.all().order_by("-id")[0].id)
    except IndexError:
        max_id = 0

    created_count = 0
    for i in range(count):
        student, created = Student.objects.get_or_create(id=(max_id + i + 1))
        if created:
            created_count += 1

        r1 = random.randint(0, 120)
        r2 = random.randint(0, 120)
        student.blackboard_total_time_spent = r1
        student.casper_total_time_spent = r2
        student.average_grade = (r1 + r2) / 240 + (random.randint(-20, 20) / 100)
        student.save()

    print("complete: {0}/{1} student data created".format(created_count, count))
