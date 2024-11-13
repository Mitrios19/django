from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order

class OrderFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testPASSword1234')
        self.order_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'address': '123 Main St',
            'postal_code': '12345',
            'city': 'Anytown',
        }

    def test_order_form_submission(self):
        self.client.login(username='testuser', password='testPASSword1234')
        response = self.client.post(reverse('orders:order_create'), self.order_data)
        self.assertEqual(response.status_code, 302)  # Проверяем, что запрос перенаправляется
        self.assertEqual(Order.objects.count(), 1)  # Проверяем, что заказ был создан

        # Получаем созданный заказ
        order = Order.objects.first()

        # Проверяем, что данные заказа соответствуют отправленным данным
        self.assertEqual(order.first_name, self.order_data['first_name'])
        self.assertEqual(order.last_name, self.order_data['last_name'])
        self.assertEqual(order.email, self.order_data['email'])
        self.assertEqual(order.address, self.order_data['address'])
        self.assertEqual(order.postal_code, self.order_data['postal_code'])
        self.assertEqual(order.city, self.order_data['city'])
