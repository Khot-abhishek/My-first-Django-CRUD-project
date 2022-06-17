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

    info = Student.objects.all()
    context = {
        'form': form,
        'students_info': info
    }
    return render(request, 'student_manager/index.html', context)


def update_data(request, id):
    stu_object = Student.objects.get(pk=id)
    if request.method == "POST":
        new_info = StudentRegistration(request.POST, instance=stu_object)
        if new_info.is_valid():
            new_info.save()
            return redirect('home')
    else:
        stu_info = StudentRegistration(instance=stu_object)
    context = {
        'form': stu_info,
    }
    return render(request, 'student_manager/update.html', context)


def delete_data(request, id):
    if request.method == "POST":
        del_student = Student.objects.get(pk=id)
        # print(del_student.name)
        del_student.delete()
        return redirect('home')
