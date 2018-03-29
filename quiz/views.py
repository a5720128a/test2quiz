from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from quiz.models import Quiz, Question

# Create your views here.

def home_page(request):
    quiz_ = Quiz.objects.all
    return render(request, 'home.html', {'quiz': quiz_})
