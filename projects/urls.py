from django.urls import path
from projects import views

urlpatterns = [
 path("list/", views.projects_list_view, name="list"),
 path('experience/', views.experience_view, name='experience'),
 path('skills/', views.skills_view, name='skills'),
]
