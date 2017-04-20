from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from .forms import Login, Sing_in
from musicants.forms import MusicantForm
from musicants.models import Musicant
from django.contrib.auth.models import User


@csrf_exempt
def index(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        print(request.user.id)
        return render(request, 'index.html', locals())


@csrf_exempt
def login(request):
    context = {'title': 'Вхад на сайт'}
    form_login = Login(request.POST or None)
    if request.method == "POST" and form_login.is_valid():
        new_form = form_login.save()
        username = form_login.cleaned_data['name']
        password = form_login.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Правильный пароль и пользователь "активен"
            auth.login(request, user)
            # Перенаправление на "правильную" страницу
            return HttpResponseRedirect('/musicants/login_musicant/%s' % user.id)
        else:
            context = {'title': 'Вхад на сайт',
                        'msg': "Введите правильный пароль или логин"}
            return render(request, 'login.html', locals())

    return render(request, 'login.html', locals())


@csrf_exempt
def sing_in(request):
    context = 'Регистрация на сайте'
    form_login = Sing_in(request.POST or None)
    if request.method == "POST" and form_login.is_valid():
        print(form_login.cleaned_data)
        new_form = form_login.save()
        username = form_login.cleaned_data['name']
        email = form_login.cleaned_data['email']
        password = form_login.cleaned_data['password']
        #create new user
        user = User.objects.create_user(username=username,
                                        email=email,
                                        password=password)
        user.is_staff = True
        user.save()
    return render(request, 'login.html', locals())


