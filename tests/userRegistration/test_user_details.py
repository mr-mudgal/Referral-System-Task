from unittest import TestCase

from django.urls import reverse

from ReferralSystemAPITask.userRegistration.models import UserRegistrationModel


class UserDetailsViewTest(TestCase):
    def test_displays_user_details(self):
        user = UserRegistrationModel.objects.create(
            email='test@example.com',
            password='password123'
        )
        data = {
            'email': user.email,
            'password': 'password123'
        }
        response = self.client.post(reverse('user_details'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-details.html')
        self.assertEqual(response.context['users']['email'], user.email)

    def test_invalid_credentials(self):
        data = {
            'email': 'wrong@email.com',
            'password': 'invalid'
        }
        response = self.client.post(reverse('user_details'), data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User Not Found')
