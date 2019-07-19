from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from django.test import Client


class AuthLayoutsTest(TestCase):

    def test_login_layout(self):
        client = Client()
        response = client.get(reverse_lazy('admin:login'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'material/login.html')
        self.assertIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="container"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="breadcrumbs"', response._container[0].decode('utf-8'))

    def test_logout_layout(self):
        client = Client()
        user = get_user_model().objects.create(
            username='test',
            email='test@test.com',
            password='123qaz123!A',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        client.force_login(user)
        response = client.get(reverse_lazy('admin:logout'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'material/logout.html')
        self.assertIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertIn(
            'Thanks for spending some quality time with the Web site today', response._container[0].decode('utf-8')
        )
        self.assertNotIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="container"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="breadcrumbs"', response._container[0].decode('utf-8'))

    def test_permission_denied_layout(self):
        client = Client()
        user = get_user_model().objects.create(
            username='test',
            email='test@test.com',
            password='123qaz123!A',
            is_staff=True,
            is_active=True
        )
        client.force_login(user)
        response = client.get('/en/admin/auth/user/')

        self.assertEqual(response.status_code, 403)
        self.assertIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertIn(
            'You have no permissions to do this action', response._container[0].decode('utf-8')
        )
        self.assertNotIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="container"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="breadcrumbs"', response._container[0].decode('utf-8'))
