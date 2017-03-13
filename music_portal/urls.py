from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^musicants/', include('musicants.urls')),
    url(r'^admin/', admin.site.urls),
]
