from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse


class LibroPermissionTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='bibliotecario',
            password='test-password',
        )

    def test_anonymous_user_is_redirected_to_cuentas_login(self):
        response = self.client.get(reverse('libro_list'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('libro_list')}",
            fetch_redirect_response=False,
        )

    def test_cuentas_root_redirects_to_login(self):
        response = self.client.get('/cuentas/', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.request['PATH_INFO'], reverse('login'))

    def test_home_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse('home'))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('home')}",
            fetch_redirect_response=False,
        )

    def test_registered_user_can_log_in_and_see_home(self):
        response = self.client.post(
            reverse('login'),
            {'username': 'bibliotecario', 'password': 'test-password'},
        )

        self.assertRedirects(response, reverse('home'))
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sesión iniciada como')
        self.assertContains(response, 'bibliotecario')

    def test_authenticated_user_without_permission_gets_forbidden(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('libro_list'))

        self.assertEqual(response.status_code, 403)

    def test_user_with_view_permission_can_open_book_list(self):
        permission = Permission.objects.get(
            content_type__app_label='catalogo',
            codename='view_libro',
        )
        self.user.user_permissions.add(permission)
        self.client.force_login(self.user)

        response = self.client.get(reverse('libro_list'))

        self.assertEqual(response.status_code, 200)
