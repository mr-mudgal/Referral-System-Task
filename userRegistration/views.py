from django.shortcuts import render, HttpResponse, redirect
from .forms import UserForm
from .models import UserRegistrationModel


def register_user(request):
    """This API function is used to register new user, and if the user uses a referral code then it increases the referral point of the referred user by 1.
    It also give error if email id is not unique or some error occurred.
    While registering it also creates a unique id automatically for referral purposes."""
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            try:
                user = UserRegistrationModel.objects.create(
                    full_name=form_data['full_name'],
                    email=form_data['email'],
                    password=form_data['password']
                )

                if form_data['referral_code'] != '':
                    other_user = UserRegistrationModel.objects.get(unique_id=form_data['referral_code'])
                    other_user.points += 1
                    other_user.save()
                    return redirect(f'/thank_you/{user.unique_id}')
            except:
                return HttpResponse(
                    '<script>alert(\'Email Id already exist or some error\'); window.open(\'/register/\', \'_self\')</script>')
        else:
            return HttpResponse('Some Error')
    else:
        form = UserForm()
    return render(request, 'register-user.html', {'form': form})


def thank_you(request, userid=''):
    """This api function simply renders the thank you page while giving user their unique id, which is also their referral id"""
    return render(request, 'Thank You.html', {'userID': userid})


def user_details(request):
    """This api function retrieves the user details after user sign in using email and password. It also displays a front-end button to view the referrals who used the current user code.
    This list of referrals is retreived from different function."""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = UserRegistrationModel.objects.get(email=email, password=password)
            userDetails = {
                'email': user.email,
                'full_name': user.full_name,
                'referral_code': user.unique_id,
                'register_time': user.registered_on
            }
            return render(request, 'user-details.html', {'users': userDetails})
        except:
            return HttpResponse(
                '<script>alert(\'User Not Found or some error\'); window.open(\'/user-details/\', \'_self\')</script>')
    return render(request, 'user-details.html', {'users': None})


def home(request):
    """Rending home page html page when on the parent route"""
    return render(request, 'home.html')


def view_my_referrals(request, code=''):
    """This api function is used to retrieve list of all the users who used a particular referral code which is passed in the url parameter"""
    try:
        print(code)
        user = UserRegistrationModel.objects.filter(referral_code=code)
        print(user)
        return render(request, 'my-referrals.html', {'users': user})
    except:
        return HttpResponse(
            f'<script>alert(\'Wrong referral code or some error\'); window.open(\'/user-details/\', \'_self\')</script>')
