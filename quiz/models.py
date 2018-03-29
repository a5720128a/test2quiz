import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Quiz(models.Model):
    quiz_text = models.CharField(max_length=200)
    user_text = models.CharField(max_length=200)
    user_point = models.IntegerField(default=0)
    def __str__(self):
        return self.quiz_text

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    # correct_answer 1 = true correct , 2 = false correct
    correct_answer = models.IntegerField(default=0)
    points_correct = models.IntegerField(default=0)
    points_incorrect = models.IntegerField(default=0)
    def __str__(self):
        return self.question_text

    
