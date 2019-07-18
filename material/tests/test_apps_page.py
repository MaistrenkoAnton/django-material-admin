from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from django.test import Client


class AppsLayoutsTest(TestCase):

    def test_login_superuser_layout(self):
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
        response = client.get(reverse_lazy('admin:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'material/index.html')
        self.assertNotIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertIn('id="container"', response._container[0].decode('utf-8'))
        self.assertIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertIn('class="breadcrumbs"', response._container[0].decode('utf-8'))
        self.assertIn('class="app-list"', response._container[0].decode('utf-8'))

    def test_login_restricted_staff_user_layout(self):
        client = Client()
        user = get_user_model().objects.create(
            username='test',
            email='test@test.com',
            password='123qaz123!A',
            is_staff=True,
            is_active=True
        )
        client.force_login(user)
        response = client.get(reverse_lazy('admin:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, 'material/index.html')
        self.assertNotIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertIn('id="container"', response._container[0].decode('utf-8'))
        self.assertIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertIn('class="breadcrumbs"', response._container[0].decode('utf-8'))
        self.assertIn('class="app-list"', response._container[0].decode('utf-8'))
        self.assertIn(
            'You don\'t have permission to view or edit anything.', response._container[0].decode('utf-8')
        )
