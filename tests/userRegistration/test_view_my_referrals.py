from unittest import TestCase

from django.urls import reverse

from ReferralSystemAPITask.userRegistration.models import UserRegistrationModel


class ViewMyReferralsViewTest(TestCase):
    def test_displays_referrals(self):
        referral_code = 'some_referral_code'
        user1 = UserRegistrationModel.objects.create(referral_code=referral_code)
        user2 = UserRegistrationModel.objects.create(referral_code=referral_code)
        response = self.client.get(reverse('view_my_referrals', kwargs={'code': referral_code}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my-referrals.html')
        self.assertEqual(list(response.context['users']), [user1, user2])

    def test_invalid_referral_code(self):
        response = self.client.get(reverse('view_my_referrals', kwargs={'code': 'invalid_code'}))
        self.assertEqual(response.status_code, 200)
