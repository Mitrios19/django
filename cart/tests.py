# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Product, Category
from django.conf import settings
from decimal import Decimal



class CartTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='TestCategory', slug='test-category')
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            slug='test-product',
            price=100.00,
            available=True
        )
        self.cart_url = reverse('cart:cart_add', args=[self.product.id])
        self.cart_detail_url = reverse('cart:cart_detail')

    def test_add_to_cart(self):
        # Отправка POST-запроса для добавления товара в корзину
        response = self.client.post(self.cart_url, {'quantity': 1, 'override': False})

        # Проверка перенаправления после добавления товара
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.cart_detail_url)

        # Проверка, что товар добавлен в корзину
        session = self.client.session
        cart = session.get(settings.CART_SESSION_ID)
        self.assertIsNotNone(cart)
        self.assertIn(str(self.product.id), cart)
        self.assertEqual(cart[str(self.product.id)]['quantity'], 1)
        self.assertEqual(Decimal(cart[str(self.product.id)]['price']), Decimal(self.product.price))
