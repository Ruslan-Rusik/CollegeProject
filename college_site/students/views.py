from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import CreateView, ListView
from .models import Student, Profile
from .form import StudentForm, RegisterForm, ProfileForm
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



# Create your views here.

# @login_required
def students(request):
    context = Student.objects.all()
    
    return render(request, 'main.html', {"students": context})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(request, "detail.html", {"student": student})


def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('main')
        


    else:
        form = StudentForm
        return render(request, 'create.html', context={'form': form})

def update_student(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
            # return reverse()
        
    else:
        form = StudentForm(instance=obj)
        return render(request, 'create.html', context={'form': form})
    

def delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('main')


def register(request):
    form = RegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            print("Проверка USERNAME:", form.cleaned_data["username"])
            user = User.objects.create_user(
                username = form.cleaned_data["username"],
                email = form.cleaned_data["email"],
                password = form.cleaned_data["password"],
            )
            login(request, user)
            return redirect('profile')
        
        else:
            context = {'form': form} 
            return render(request, 'registration/register.html', context=context)
        
    else: 
        context = {'form': form}
        return render(request, 'registration/register.html', context=context)
    

def profile(request): 
    if request.method == "POST":
        form = ProfileForm(request.POST)   
        
        if form.is_valid():
            obj = form.save(commit=False)  # Временный объект без id
            obj.user = request.user
            obj.email = request.user.email
            obj.name = request.user.username
            obj.save()  # Сохраняем объект с данными и его id
            form.save_m2m()  # Благодаря тому, что таблица profile поимела id, мы можем связать ее с другими таблицами по связи m2m
            return redirect('main')
        
        else:
            context = {'form': form} 
            return render(request, 'registration/profile.html', context=context)

    else:
        form = ProfileForm()  
        context = {'form': form}
        return render(request, 'registration/profile.html', context=context)
    

def detail_profile(request):
    user = request.user
    profile = Profile.objects.filter(user=user)

    return render(request, 'see_profile.html', {'profile': profile})

def myOwnLogoutView(request):
    if request.method == "GET":
        logout(request)
        return redirect('login')