from django.db import models


class Student(models.Model):
    blackboard_total_time_spent = models.IntegerField(default=0)
    casper_total_time_spent = models.IntegerField(default=0)
    average_grade = models.FloatField(default=0)

    def __str__(self):
        return str(self.id)


class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=8)
    grade = models.FloatField(default=0)
