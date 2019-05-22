from django.test import (
    Client,
    TestCase,
    RequestFactory,
)
from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from products.models import Product
from products.views import (
    product_view,
)
from users.models import User


class ProductViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='john')
        self.user.set_password('smith')
        self.user.save()
        self.product = Product.objects.create(name="table", status="ST", quantity=234)

    def login_client(self):
        self.client.post('/', {'username': 'john', 'password': 'smith'})

    def login_client2(self):
        self.client.login(username='john', password='smith')

    def test_product_view__200(self):
        self.login_client()
        response = self.client.get(f'/products/view/{self.product.id}')
        self.assertEqual(response.status_code, 200)

    def test_product_view__404(self):
        self.login_client2()
        response = self.client.get(f'/products/view/{self.product.id+1}')
        self.assertEqual(response.status_code, 404)

    def test_product_view__302(self):
        response = self.client.get(f'/products/view/{self.product.id+1}')
        self.assertEqual(response.status_code, 302)


class ProductViewsTestCase2(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')
        self.product = Product.objects.create(name="table", status="ST", quantity=234)

    def login_request(self, request):
        request.user = self.user
        return request

    def anonymous_user(self, request):
        request.user = AnonymousUser()
        return request

    def test_product_view__200(self):
        request = self.factory.get('/products/view/')
        request = self.login_request(request)
        response = product_view(request, self.product.id)
        # Use this syntax for class-based views.
        # response = ProductView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_product_view__404(self):
        with self.assertRaises(Http404):
            request = self.factory.get('/products/view/')
            request = self.login_request(request)
            response = product_view(request, self.product.id+1)
            # Use this syntax for class-based views.
            # response = ProductView.as_view()(request)

    def test_product_view__302(self):
        request = self.factory.get('/products/view/')
        request = self.anonymous_user(request)
        response = product_view(request, self.product.id)
        # Use this syntax for class-based views.
        # response = ProductView.as_view()(request)
        self.assertEqual(response.status_code, 302)

