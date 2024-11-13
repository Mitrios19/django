# tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from shop.models import Product, Review, Category


class ReviewTest(TestCase):
    def setUp(self):
        # Создание пользователя
        self.user = User.objects.create_user(username='testuser', password='testPASSword1234')

        # Создание категории
        self.category = Category.objects.create(name='TestCategory', slug='test-category')

        # Создание продукта
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=100.00,
            available=True
        )

        # Данные для отзыва
        self.review_data = {
            'rating': 5,
            'comment': 'Great product!',
        }

    def test_create_review(self):
        # Авторизация пользователя
        self.client.login(username='testuser', password='testPASSword1234')

        # Создание отзыва
        response = self.client.post(
            reverse('shop:product_detail', kwargs={'id': self.product.id, 'slug': self.product.slug}), self.review_data)
        self.assertEqual(response.status_code, 302)  # Проверяем, что запрос перенаправляется

        # Проверка, что отзыв был создан
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.rating, self.review_data['rating'])
        self.assertEqual(review.comment, self.review_data['comment'])
