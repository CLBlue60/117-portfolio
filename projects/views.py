from django.shortcuts import render, redirect
from .models import Project, Experience, Skill
from .forms import ProjectForm
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

def projects_list_view(request):
    projects = Project.objects.all().order_by('-year')
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    return render(request, 'projects/projects_list.html', {"projects": projects, "form": form})

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    return redirect('list')

def experience_view(request):
    experiences = Experience.objects.all()
    return render(request, 'projects/experience.html', {'experiences': experiences})

def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'pages/skills.html', {'skills': skills})
