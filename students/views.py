from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Student


class HomePageView(TemplateView):
    template_name = "home.html"


class StudentsPageView(ListView):
    model = Student
    template_name = "students.html"
    context_object_name = "all_students_list"


class StudentCreateView(CreateView):
    model = Student
    template_name = "student_new.html"
    fields = ["id", "first_name", "last_name"]
    success_url = "/students/"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_edit.html"
    fields = ["first_name", "last_name"]
    success_url = "/students/"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = "/students/"