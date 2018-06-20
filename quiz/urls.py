from django.urls import path

from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('<int:quiz_id>/', views.detail, name='detail'),
    path('add_quiz', views.add_quiz, name='add_quiz'),
]
