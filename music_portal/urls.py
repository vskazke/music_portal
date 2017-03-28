from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
#  from django.contrib.auth.views import login, logout
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^musicants/', include('musicants.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
    #  url(r'^accounts/login/$',  TemplateView.as_view(template_name="login.html")),
    #  url(r'^accounts/logout/$', logout),
]
