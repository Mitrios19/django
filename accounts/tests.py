from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testPASSword1234!')
    def test_SignUp(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testPASSword1234!',
        })
        self.assertEqual(response.status_code, 302)


class ChangeUsernameTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='oldusername', password='testpassword')

    def test_change_username(self):
        self.client.login(username='oldusername', password='testpassword')
        new_username = 'newusername'
        response = self.client.post(reverse('user:change_username'), {'username': new_username})
        self.assertEqual(response.status_code, 302)  # Проверяем, что запрос перенаправляется
        self.user.refresh_from_db()  # Обновляем данные о пользователе из базы данных
        self.assertEqual(self.user.username, new_username)  # Проверяем, что логин был изменен
