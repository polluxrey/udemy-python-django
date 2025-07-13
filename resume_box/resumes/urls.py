from django.urls import path
from .views import ResumeCreateView

app_name = "resumes"

urlpatterns = [
    path('', ResumeCreateView.as_view(), name="home"),
]
