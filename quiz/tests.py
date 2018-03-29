from django.urls import resolve
from django.test import TestCase
from quiz.models import Quiz, Question

# Create your tests here.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class QuizAndQuestionModelsTest(TestCase):

    def test_saving_and_retrieving_questions(self):

        quiz_ = Quiz()
        quiz_.save()

        first_question = Question()
        first_question.question_text = 'The first (ever) quiz Question'
        first_question.quiz = quiz_
        first_question.save()

        second_question = Question()
        second_question.question_text = 'Question the second'
        second_question.quiz = quiz_
        second_question.save()

        saved_quiz = Quiz.objects.first()
        self.assertEqual(saved_quiz, quiz_)

        saved_questions = Question.objects.all()
        self.assertEqual(saved_questions.count(), 2)

        first_saved_question = saved_questions[0]
        second_saved_question = saved_questions[1]
        self.assertEqual(first_saved_question.question_text, 'The first (ever) quiz Question')
        self.assertEqual(first_saved_question.quiz, quiz_)
        self.assertEqual(second_saved_question.question_text, 'Question the second')
        self.assertEqual(second_saved_question.quiz, quiz_)
