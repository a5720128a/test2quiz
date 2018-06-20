from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from quiz.models import Quiz, Question, User

# Create your views here.

def home_page(request):
    quiz_ = Quiz.objects.all
    d_message = ""
    return render(request, 'home.html', {'quiz': quiz_, 'd_message': d_message})

def detail(request, quiz_id):
    d_message = ""
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, 'detail.html', {'quiz': quiz, 'd_message': d_message})

def add_quiz(request):
    d_message = ""
    quizs = Quiz.objects.all
    quiz_reference = str(request.POST['quiz_input'])
    # query for duplicate quiz
    d_query = Quiz.objects.filter(quiz_text=quiz_reference)
    if (not d_query) and (quiz_reference != '') :
        quiz_ = Quiz.objects.create(quiz_text = request.POST['quiz_input'])
        return redirect('/')
    else :
        d_message = "duplicate or null quiz, please enter new quiz."
        return render(request, 'home.html', {'quizs': quizs, 'd_message': d_message})

def add_question(request, quiz_id):
    quiz_ = Quiz.objects.get(id=quiz_id)
    question_reference = str(request.POST['question_input'])
    correct_answer_reference = str(request.POST['correct_input'])
    # query for duplicate question
    d_query = Question.objects.filter(question_text=question_reference, quiz=quiz_)
    if (not d_query) and (question_reference != '') :
        question_ = Question.objects.create(question_text=request.POST['question_input'], correct_answer = correct_answer_reference, points_correct = 0, points_incorrect = 0, quiz=quiz_)
        return redirect('/%d/' % (quiz_.id,))
    else :
        d_message = "duplicate or null question, please enter new question."
        return render(request, 'detail.html', {'quiz': quiz_, 'd_message': d_message})

def submit(request, quiz_id):
    d_message = ""
    quiz_ = Quiz.objects.get(id=quiz_id)
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question_amount = Question.objects.filter(quiz=quiz_).count()+1
    stat = []
    point = 0
    for i in range(1,question_amount):
        try:
            selected_choice = str(request.POST['choice '+str(i)]).split(':')
            selected_choice_value = selected_choice[0]
            question_id = selected_choice[1]
            question_ = Question.objects.get(id=question_id)
            # correct_answer 1 = true correct , 2 = false correct
            correct_answer = Question.objects.get(pk=question_id).correct_answer
            if str(selected_choice_value) == str(correct_answer) :
                point = point+1
                stat.append(question_id)
                question_.points_correct = question_.points_correct+1
                question_.save()
            else :
                question_.points_incorrect = question_.points_incorrect+1
                question_.save()
        except :
            pass
    all_stat = ':'.join(map(str, stat))
    print(stat)
    user_reference = str(request.POST['user_input'])
    user_ = User.objects.create(user_text = user_reference, user_point=point, stat=all_stat, quiz2 = quiz_)
    
    return render(request, 'result.html', {'quiz': quiz, 'stat': stat, 'user_reference': user_reference, 'point': point})

