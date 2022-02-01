from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import RegisterForm


class RegisterView(FormView):
    """ Регистрация пользователя """

    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = 'login/'

    def form_valid(self, form):
        form.save()
        login(self.request, form)
        # return super(RegisterView, self).form_valid(form)
        return redirect('/')

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)


class LoginView(LoginView):
    """ Логин """
    form_class = AuthenticationForm
    template_name = 'account/login.html'
    success_url = '/'

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


def logout_user(request):
    """ Выход """
    logout(request)
    return redirect('/account/login')
