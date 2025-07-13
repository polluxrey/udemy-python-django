from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import ResumeModel
from .forms import ResumeForm

# Create your views here.


class ResumeCreateView(CreateView):
    model = ResumeModel
    form_class = ResumeForm
    success_url = reverse_lazy("resumes:home")

    def form_valid(self, form):
        messages.success(self.request, "Resume uploaded successfully!")
        return super().form_valid(form)