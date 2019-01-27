from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from accounts.forms import Account_Form, Registration_Form, Registration_Model_Form
from accounts.models import Account
from server import settings
from django.http import HttpResponse, HttpResponseRedirect
import random, hashlib

def profile(request, pk):
    acc = get_object_or_404(Account, pk=pk)

    return render(request, "accounts/profile.html", {'instance': acc})


def login_view(request):
    success_url = reverse_lazy('main:main')
    if request.method == 'POST':
        usr = request.POST.get('username')
        psw = request.POST.get('password')
        user = authenticate(username=usr, password=psw)

        if user and user.is_active:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend' )
            return redirect(success_url)

    return render(request, 'accounts/login.html')


def logout_view(request):
    success_url = reverse_lazy('main:main')
    logout(request)
    return redirect(success_url)


@login_required(login_url=reverse_lazy('accounts:login'))
def confirm_account(request):
    success_url = reverse_lazy('main:main')
    request.user.is_active=True

    return redirect(success_url)


def verify(request, email, activation_key):
    try:
        user = Account.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active=True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print( f'error activation user: {user} ' )
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user: {e.args}')
        return HttpResponseRedirect(reverse('main:main'))


def registration(request):
    template_name = "accounts/registration.html"
    success_url = reverse_lazy('accounts:login')
    form = Registration_Model_Form(request.POST)
    if request.method == 'POST':
        form = Registration_Model_Form(data=request.POST)
        if form.is_valid():
            user = form.save()
            salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
            user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
            verify_link = reverse('accounts:verify', args=[user.email, user.activation_key])
            login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')

            send_mail(
                'Registration User',
                f'Для подтверждения учетной записи {user.username} на портале \ перейдите по ссылке: http://localhost:8000{verify_link}',
                from_email='info@project.ru',
                recipient_list=[user.email],
                fail_silently=False
            )

            return redirect(success_url)

    return render(request, template_name, {'form': form})


def account_update(request, pk):
    template_name = "accounts/registration.html"
    success_url = reverse_lazy('accounts:login')
    acc = get_object_or_404(Account, pk=pk)
    form = Account_Form(instance=acc)

    if request.method == 'POST':
        form = Account_Form(
            request.POST,
            instance=acc
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(request, template_name, {'form': form})


def account_delete(request, pk):
    template_name = "accounts/delete.html"
    success_url = reverse_lazy('main:main')
    acc = get_object_or_404(Account, pk=pk)

    if request.method == 'POST':
        acc.delete()

        return redirect(success_url)

    return render(request, template_name, {'instance': acc})
