from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render

from .forms import MusicantForm
from .models import Musicant
from django.contrib.auth.models import User


def musicant_home_page(request, user_id):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    elif int(request.user.id) == int(user_id):
        print(request.user.id, user_id)
        try:
            Login_musicant = User.objects.get(id=user_id)
            #  musicants_list = Musicant.objects.get(musicant=Login_musicant)
            #  musicants_list = Musicant.objects.all()
            #  print(musicants_list[1])
        except User.DoesNotExist:
            raise Http404("Musicant is not login")
        musicants_list = Login_musicant.musicant_set.all()
    else:
        raise Http404("This page is not available for musicant")
    return render(request, 'login_musicant_list.html', locals())


def new_musicant(request):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        print(request.user.password)
        q = User.objects.get(id=request.user.id)
        print(q.id)
        print(q.musicant_set.all())
        form = MusicantForm(request.POST or None)
        if request.method == "POST" and form.is_valid():
            musicant = Musicant(name=form.cleaned_data['name'],
                                musicant=q,
                                email=form.cleaned_data['email'],
                                type_of_music=form.cleaned_data['type_of_music'],
                                instrument=form.cleaned_data['instrument'],
                                level=form.cleaned_data['level'])
            if 'save' in request.POST:
                musicant.save()
                return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)
            elif 'public' in request.POST:
                musicant.public = True
                print(musicant.public)
                musicant.save()
                return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)

        return render(request, 'new_musicant.html', locals())


def musicant_detail_notice(request, musicant_id):
    if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        q = User.objects.get(id=request.user.id)
        print(q)
    try:
        musicant = Musicant.objects.get(pk=musicant_id)
    except Musicant.DoesNotExist:
        raise Http404("Question does not exist")
    instrument = musicant.instrument.split("'")
    print(instrument, q)
    data = {'name': musicant.name,
            #  'musicant': q,
            'email': musicant.email,
            'type_of_music': musicant.type_of_music,
            'instrument': instrument,
            'level': musicant.level}
    form = MusicantForm(request.POST or None, initial=data)
    if musicant.public:
        print('rrrr')
    print(musicant.public)
    if request.method == "POST" and form.is_valid():
        musicant = Musicant.objects.get(pk=musicant_id)
        musicant.name = form.cleaned_data['name']
        musicant.email = form.cleaned_data['email']
        musicant.type_of_music = form.cleaned_data['type_of_music']
        musicant.instrument = form.cleaned_data['instrument']
        musicant.level = form.cleaned_data['level']
        if 'save' in request.POST:
            musicant.save()
            return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)
        elif 'public' in request.POST:
            musicant.public = True
            musicant.save()
            return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)
        elif 'unpublic' in request.POST:
            musicant.public = False
            musicant.save()
            return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)
        elif 'delete' in request.POST:
            musicant.delete()
            return HttpResponseRedirect('/musicants/login_musicant/%s' % q.id)

        #  p = Musicant(data)
        #  form.save()
    return render(request, 'notice.html', locals())


def musicants_list(request):
    #  musicants_list = Musicant.objects.order_by('-pub_date')
    musicants_list = []
    musicants = Musicant.objects.all()
    for musicant in musicants:
        if musicant.public:
            musicants_list.append(musicant)
    #  context = {'musicant_list': musicants_list}
    return render(request, 'musicants_list.html', {'musicants_list': musicants_list})


def detail_notice(request, musicant_id):
    try:
        musicant = Musicant.objects.get(pk=musicant_id)
    except Musicant.DoesNotExist:
        raise Http404("Question does not exist")
    #  instrument = musicant.instrument.split("'")
    data = {'name': musicant.name,
            #  'musicant': q,
            'email': musicant.email,
            'type_of_music': musicant.type_of_music,
            'instrument': musicant.instrument,
            'level': musicant.level}
    form = MusicantForm(initial=data)
    return render(request, 'detail_notice.html', locals())



#  def musicants(request):
    #  return HttpResponse("Hello, world. You're at the polls index.")
