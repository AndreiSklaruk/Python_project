from django.contrib import auth  # Добавление авторизации
from django.shortcuts import HttpResponseRedirect  # Добавление перенаправления
from django.urls import reverse, reverse_lazy  # Добавление обратных ссылок
from products.models import Basket  # Добавление модели корзины
from users.models import User, EmailVerification  # Добавление модели пользователя
from django.views.generic.edit import CreateView, UpdateView  # Добавление регистрации и обновления данных
from django.contrib.auth.views import LoginView  # Добавление авторизации
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm  # Добавление форм
from django.contrib.messages.views import SuccessMessageMixin  # Добавление сообщения об успешном изменении данных
from common.views import TitleMixin  # Добавление заголовка
from django.views.generic import TemplateView  # Добавление подтверждения почты



class UserLoginView(TitleMixin, LoginView):  # Авторизация пользователя
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'  # Добавление заголовка


class UserRegistrationView(SuccessMessageMixin, CreateView):  # Регистрация пользователя
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались!'

    def get_context_data(self, **kwargs):  # Добавление заголовка
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(TitleMixin, UpdateView):  # Обновление данных пользователя
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    title = 'Store - Личный кабинет'

    def get_success_url(self):  # Переопределение метода для вывода сообщения об успешном изменении данных
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})




def logout(request):  # Выход из учетной записи - не обязательный класс, так как прописан LOGOUT_REDIRECT_URL = '/'
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class EmailVerificationView(TitleMixin, TemplateView, ):  # Подтверждение почты
    objects = None
    title = 'Подтверждение почты'
    template_name = 'users/email_verification.html'


def get(self, request, *args, **kwargs):  # Переопределение метода get
    code = kwargs.get('code')
    user = User.objects.get(email=kwargs.get('email'))
    email_verification = EmailVerification.objects.filter(user=user, code=code)

    if email_verification.exists() and not email_verification.first().is_expired():
        user.is_verified_email = True
        user.save()
        expiration = email_verification.first().expiration
        return super(EmailVerificationView, self).get(request, *args, **kwargs)
    else:
        return HttpResponseRedirect(reverse('index'))
