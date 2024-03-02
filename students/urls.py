from django.urls import path
from .views import (
    HomePageView,
    StudentsPageView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("students/", StudentsPageView.as_view(), name="students"),
    path("students/new/", StudentCreateView.as_view(), name="student_new"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student_edit"),
    path(
        "students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"
    ),
]