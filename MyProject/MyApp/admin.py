from django.contrib import admin
from .models import Student, Instructor, Course, Department, Classroom, Enrollment

admin.site.register(Student);
admin.site.register(Instructor);
admin.site.register(Course);
admin.site.register(Department);
admin.site.register(Classroom);
admin.site.register(Enrollment);
