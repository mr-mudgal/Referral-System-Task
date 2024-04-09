from django.test import TestCase
from django.urls import reverse

from ReferralSystemAPITask.userRegistration.models import UserRegistrationModel


class RegisterUserViewTest(TestCase):
    def test_registration_successful(self):
        data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'password': 'password123'
        }
        response = self.client.post(reverse('register_user'), data)
        self.assertEqual(response.status_code, 302)  # Redirect on success
        self.assertRedirects(response, reverse('thank_you'))

        # Assert user was created in the database
        user = UserRegistrationModel.objects.get(email='test@example.com')
        self.assertEqual(user.full_name, 'Test User')

    def test_registration_failed_email_exists(self):
        UserRegistrationModel.objects.create(email='test@example.com')
        data = {
            # ... same data as above
        }
        response = self.client.post(reverse('register_user'), data)
        self.assertEqual(response.status_code, 200)  # Error displayed on failure
        self.assertContains(response, 'Email Id already exist')

