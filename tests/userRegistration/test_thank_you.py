from unittest import TestCase

from django.urls import reverse


class ThankYouViewTest(TestCase):
    def test_renders_thank_you_page(self):
        user_id = 'some_unique_id'
        response = self.client.get(reverse('thank_you', kwargs={'userid': user_id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Thank You.html')
        self.assertEqual(response.context['userID'], user_id)
