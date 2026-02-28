from django.db import models


class Department(models.Model):
    dep_code = models.CharField(max_length=5, primary_key=True)
    dep_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dep_name


class Course(models.Model):
    course_code = models.CharField(max_length=8, primary_key=True)
    course_title = models.CharField(max_length=40)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_title


class Instructor(models.Model):
    instructor_id = models.AutoField(primary_key=True)
    instructor_name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.instructor_name


class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30)
    s_cgpa = models.FloatField(null=True, blank=True)
    s_dob = models.DateField()
    s_address = models.CharField(max_length=50, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name


class Classroom(models.Model):
    crn = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=15)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    max_enrollment = models.IntegerField()
    room = models.CharField(max_length=8)
    days = models.CharField(max_length=4)
    time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course} - {self.semester}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'classroom')

    def __str__(self):
        return f"{self.student} - {self.classroom}"