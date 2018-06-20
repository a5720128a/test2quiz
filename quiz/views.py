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
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist")
    return render(request, 'detail.html', {'quiz': quiz})

def add_quiz(request):
    d_message = ""
    quizs = Quiz.objects.order_by('-date_pub')[:5]
    quiz_reference = str(request.POST['quiz_input'])
    # query for duplicate quiz
    d_query = Quiz.objects.filter(quiz_text=quiz_reference)
    if (not d_query) and (quiz_reference != '') :
        quiz_ = Quiz.objects.create(quiz_text = request.POST['quiz_input'])
        return redirect('/')
    else :
        d_message = "duplicate quiz name or empty ,please fill another quiz name."
        return render(request, 'home.html', {'quizs': quizs, 'd_message': d_message})


'''
def submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    try:
        selected_choice = quiz.question_set.get(pk=request.POST['choice'])
        # correct_answer 1 = true correct , 2 = false correct
        correct_answer = quiz.question_set.get(pk=correct_answer)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the quiz voting form.
        return render(request, 'detail.html', {
            'quiz': quiz,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice = correct_answer
            User.user_point += 1
            user.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('quiz:results', args=(quiz.id,)))
'''
