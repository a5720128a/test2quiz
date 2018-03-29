from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from quiz.models import Quiz, Question, User

# Create your views here.

def home_page(request):
    quiz_ = Quiz.objects.all
    return render(request, 'home.html', {'quiz': quiz_})

def detail(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Question.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, 'detail.html', {'quiz': quiz})
