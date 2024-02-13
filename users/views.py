import random

from django.core.checks import messages
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from config import settings
from users.forms import UserRegisterForm, UserUpdateForm, NewPasswordForm
from users.models import User


# class RegisterView(CreateView):
#     model = User
#     form_class = UserRegisterForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         new_user = form.save()
#         send_mail(
#             subject='Welcome to our service',
#             message='Вы зарегистрировались в нашем сервисе!',
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[new_user.email]
#         )
#         return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import CreateView


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.is_active = False  # Новый пользователь неактивен до подтверждения почты
        new_user.save()

        # Отправка письма с подтверждением
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account'
        message = self.render_email_message(new_user, current_site)
        to_email = form.cleaned_data.get('email')
        send_mail(mail_subject, message, settings.EMAIL_HOST_USER, [to_email])

        return super().form_valid(form)

    def render_email_message(self, user, current_site):
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        return f"Please click the link below to verify your email address: \
                http://{current_site.domain}/users/verify-email/{uid}/{token}/"


class VerifyEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user_model = get_user_model()
            user = user_model.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, user_model.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            # Если пользователь найден и токен действителен, установите его статус email_verified в True и сохраните пользователя
            user.is_active = True
            user.save()
            # Выполните вход пользователя
            login(request, user)
            # Перенаправьте пользователя на страницу успешной верификации
            return redirect('/users/login')
        else:
            # Если токен недействителен, вы можете перенаправить пользователя на страницу с ошибкой или сделать что-то еще
            raise Http404("/users/verify-email.html")


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            subject='Пароль изменен',
            message=f'Ваш новый пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    else:
        form = NewPasswordForm
        context = {
            'form': form
        }
        return render(request, 'users/new_password.html', context)
