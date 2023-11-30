from django.urls import path
from users.views import *
import users
from products.views import *
from django.contrib.auth.views import login_required
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('profile/<int:pk>/',login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='email_verification'),

   ]