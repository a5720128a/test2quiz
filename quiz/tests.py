from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from quiz.models import Quiz, Question, User

# Create your tests here.

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>quiz</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_displays_all_list_quiz(self):
        Quiz.objects.create(quiz_text='wordey 1')
        Quiz.objects.create(quiz_text='wordey 2')

        response = self.client.get('/')

        self.assertIn('wordey 1', response.content.decode())
        self.assertIn('wordey 2', response.content.decode())

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

class QuizAndUserModelsTest(TestCase):

    def test_saving_and_retrieving_users(self):

        quiz_ = Quiz()
        quiz_.save()

        first_user = User()
        first_user.user_text = 'The first (ever) quiz user'
        first_user.quiz2 = quiz_
        first_user.save()

        second_user = User()
        second_user.user_text = 'user the second'
        second_user.quiz2 = quiz_
        second_user.save()

        saved_quiz = Quiz.objects.first()
        self.assertEqual(saved_quiz, quiz_)

        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 2)

        first_saved_user = saved_users[0]
        second_saved_user = saved_users[1]
        self.assertEqual(first_saved_user.user_text, 'The first (ever) quiz user')
        self.assertEqual(first_saved_user.quiz2, quiz_)
        self.assertEqual(second_saved_user.user_text, 'user the second')
        self.assertEqual(second_saved_user.quiz2, quiz_)

class NewQuizTest(TestCase):
    
    def test_can_save_a_POST_request(self):
        self.client.post('/add_quiz', data={'quiz_input': 'A new list quiz'})

        self.assertEqual(Quiz.objects.count(), 1)
        new_quiz = Quiz.objects.first()
        self.assertEqual(new_quiz.quiz_text, 'A new list quiz')


    def test_redirects_after_POST(self):
        response = self.client.post('/add_quiz', data={'quiz_input': 'A new list quiz'})
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

class NewQuestionTest(TestCase):
    
    def test_can_save_a_POST_question_request_to_an_quiz(self):
        other_quiz = Quiz.objects.create()
        correct_quiz = Quiz.objects.create()

        self.client.post(
            '/%d/add_question' % (correct_quiz.id,),
            data={'question_input': 'A new question for an quiz', 'correct_input': '1'}
        )

        self.assertEqual(Question.objects.count(), 1)
        new_question = Question.objects.first()
        self.assertEqual(new_question.question_text, 'A new question for an quiz')
        self.assertEqual(new_question.quiz, correct_quiz)


    def test_redirects_to_quiz_view(self):
        other_quiz = Quiz.objects.create()
        correct_quiz = Quiz.objects.create()

        response = self.client.post(
            '/%d/add_question' % (correct_quiz.id,),
            data={'question_input': 'A new question for an quiz', 'correct_input': '1'}
        )

        self.assertRedirects(response, '/%d/' % (correct_quiz.id,))

class SubmitTest(TestCase):
    
    def test_render_after_submit(self):
        quiz_ = Quiz()
        quiz_.save()
        
        user_ = User()
        user_.user_text = 'test'
        user_.user_point += 1
        user_.quiz2 = quiz_
        user_.save()

        response = self.client.post(
            '/%d/submit' % (quiz_.id,),
            data={'user_input': 'A new user'}
        )
