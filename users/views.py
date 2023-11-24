from django.contrib import auth
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from products.models import Basket
from users.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin


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


class UserProfileView(TitleMixin,UpdateView):  # Обновление данных пользователя
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    title = 'Store - Личный кабинет'

    def get_success_url(self):  # Переопределение метода для вывода сообщения об успешном изменении данных
        return reverse_lazy('users:profile', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):  # Добавление товаров к корзину именно того пользователя, который их добавил
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


def logout(request):  # Выход из учетной записи - не обязательный класс, так как прописан LOGOUT_REDIRECT_URL = '/'
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
