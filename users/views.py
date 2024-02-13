import random
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

from config import settings
from users.forms import UserRegisterForm, UserUpdateForm, NewPasswordForm
from users.models import User


class ProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class RegisterView(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verify_email')
    template_name = 'users/register.html'

    def form_valid(self, form: UserRegisterForm):
        new_user = form.save()

        send_mail(
            subject='Подтвердите почту',
            message=f'Вернитесь на сайт и введите код подтверждения регистрации: {new_user.verify_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class VerifyCodeView(View):
    model = User
    template_name = 'users/verify_email.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        verify_code = request.POST.get('verify_code')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user.is_verified = True
            user.save()
            return redirect('users:login')

        return redirect('users:verify_email')


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
        return render(request, 'users/register.html', context)
