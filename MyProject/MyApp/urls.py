from django.urls import path
from .views import DepartmentListCreate, CourseListCreate, InstructorListCreate, StudentListCreate, ClassroomListCreate, EnrollmentListCreate

urlpatterns = [
    path('departments/', DepartmentListCreate.as_view(), name='department-list'),
    path('courses/', CourseListCreate.as_view(), name='course-list'),
    path('instructors/', InstructorListCreate.as_view(), name='instructor-list'),
    path('students/', StudentListCreate.as_view(), name='student-list'),
    path('classrooms/', ClassroomListCreate.as_view(), name='classroom-list'),
    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list'),
    path('departments/<str:dep_code>/', DepartmentListCreate.as_view(), name='department-detail'),
    path('courses/<str:course_code>/', CourseListCreate.as_view(), name='course-detail'),
    path('instructors/<int:instructor_id>/', InstructorListCreate.as_view(), name='instructor-detail'),
    path('students/<int:s_id>/', StudentListCreate.as_view(), name='student-detail'),
    path('classrooms/<int:crn>/', ClassroomListCreate.as_view(), name='classroom-detail'),
    path('enrollments/<int:pk>/', EnrollmentListCreate.as_view(), name='enrollment-detail'),
]