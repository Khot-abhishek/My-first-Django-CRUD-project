from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.


def home(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            stu_name = form.cleaned_data['name']
            stu_email = form.cleaned_data['email']
            stu_password = form.cleaned_data['password']
            student_obj = Student(
                name=stu_name, email=stu_email, password=stu_password)
            student_obj.save()
            return redirect('home')
    else:
        form = StudentRegistration()

    context = {
        'form': form
    }
    return render(request, 'student_manager/index.html', context)


def delete_data(request, stu_id):
    pass


def update_data(request, stu_id):
    pass
