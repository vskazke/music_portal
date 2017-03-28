from django.http import HttpResponse
from django.shortcuts import render

from .forms import Musicant


def musicants(request):
    form = Musicant(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
        print(form)

    return render(request, 'new_musicant.html', locals())

#  def musicants(request):
    #  return HttpResponse("Hello, world. You're at the polls index.")
