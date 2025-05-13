from django.shortcuts import render
from .models import Project, Experience, Skill


def projects_list_view(request):
    projects = Project.objects.all().order_by('-year')

    return render(request, 'projects/projects_list.html', {"projects": projects})

def experience_view(request):
    experiences = Experience.objects.all()
    return render(request, 'projects/experience.html', {'experiences': experiences})

def skills_view(request):
    skills = Skill.objects.all()
    return render(request, 'pages/skills.html', {'skills': skills})
