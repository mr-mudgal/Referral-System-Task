from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'), # api for registering user
    path('thank_you/<userid>/', views.thank_you, name='thank_you/<userid>'), # api for displaying thank you message and the userid (unique) which is also referral code, which is passed in the url parameter
    path('user-details/', views.user_details, name='user-details'), # api to fetch user details from database and display them
    path('', views.home, name='home'), # home route api
    path('view-my-referrals/<code>/', views.view_my_referrals, name='view-my-referrals/<code>'), # api to fetch all the user list who used a particular referral code which is passed in the url parameter
]
