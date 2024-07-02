from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('courses/', views.CourseApiView.as_view(), name='courses'),
    path('courses/<int:pk>/', views.CourseDetailApiView.as_view(), name='course-detail'),
    path('teachers/', views.TeacherApiView.as_view(), name='teachers'),
    path('teachers/<int:pk>/', views.TeacherDetailApiView.as_view(), name='teacher-detail'),
    path('students/', views.StudentApiView.as_view(), name='students'),
    path('students/<int:pk>/', views.StudentDetailApiView.as_view(), name='student-detail'),
    ]