from django.urls import path
from .views import DepartmentListCreate, CourseListCreate, InstructorListCreate, StudentListCreate, ClassroomListCreate, EnrollmentListCreate, EnrollmentDetail, DepartmentDetail, CourseDetail, InstructorDetail, StudentDetail, ClassroomDetail, UserCreate
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserCreate.as_view(), name='user-create'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('departments/', DepartmentListCreate.as_view(), name='department-list'),
    path('courses/', CourseListCreate.as_view(), name='course-list'),
    path('instructors/', InstructorListCreate.as_view(), name='instructor-list'),
    path('students/', StudentListCreate.as_view(), name='student-list'),
    path('classrooms/', ClassroomListCreate.as_view(), name='classroom-list'),
    path('enrollments/', EnrollmentListCreate.as_view(), name='enrollment-list'),
    path('departments/<str:dep_code>/', DepartmentDetail.as_view(), name='department-detail'),
    path('courses/<str:course_code>/', CourseDetail.as_view(), name='course-detail'),
    path('instructors/<int:instructor_id>/', InstructorDetail.as_view(), name='instructor-detail'),
    path('students/<int:s_id>/', StudentDetail.as_view(), name='student-detail'),
    path('classrooms/<int:crn>/', ClassroomDetail.as_view(), name='classroom-detail'),
    path('enrollments/<int:pk>/', EnrollmentDetail.as_view(), name='enrollment-detail'),
]