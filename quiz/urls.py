from django.urls import path, re_path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('<int:quiz_id>/', views.detail, name='detail'),
    path('add_quiz', views.add_quiz, name='add_quiz'),
    re_path(r'^(\d+)/add_question$', views.add_question, name='add_question'),
    re_path(r'^(\d+)/submit$', views.submit, name='submit'),
]
