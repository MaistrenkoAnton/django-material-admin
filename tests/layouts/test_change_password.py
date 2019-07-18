from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy
from django.test import Client


class ChangePasswordLayoutsTest(TestCase):

    def test_change_password_layout(self):
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
        response = client.get(reverse_lazy('admin:password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'material/password_change.html')
        self.assertNotIn('class="side-bar"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="login-form"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="username-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('id="password-input"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="submit-row-btn"', response._container[0].decode('utf-8'))
        self.assertIn('id="container"', response._container[0].decode('utf-8'))
        self.assertIn('id="tray"', response._container[0].decode('utf-8'))
        self.assertIn('class="scroll-pane"', response._container[0].decode('utf-8'))
        self.assertIn('class="breadcrumbs"', response._container[0].decode('utf-8'))
        self.assertNotIn('class="app-list"', response._container[0].decode('utf-8'))
        self.assertNotIn(
            'You don\'t have permission to view or edit anything.', response._container[0].decode('utf-8')
        )

    def test_change_password_with_errors_layout(self):
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
        response = client.post(reverse_lazy('admin:password_change'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], 'material/password_change.html')
        self.assertIn(
            """<div class="toast rounded error-toast panning">
                  
                  Please correct the errors below.
                  
                </div>
            """, response._container[0].decode('utf-8')
        )
        self.assertIn(
            """<button class="btn waves-effect waves-light default" type="submit" name="action">
                Change my password
                <i class="material-icons right">send</i>
              </button>
            """, response._container[0].decode('utf-8')
        )
        self.assertIn(
            '<ul class="errorlist"><li>This field is required.</li></ul>', response._container[0].decode('utf-8')
        )
