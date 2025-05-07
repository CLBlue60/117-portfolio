from django.urls import path
from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
