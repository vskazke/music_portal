from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^new_musicant/$', views.new_musicant, name='new_musicant'),
        url(r'^(?P<musicant_id>[0-9]+)/$', views.musicant_detail_notice, name='musicant_detail_notice'),
        url(r'^login_musicant/(?P<user_id>[0-9]+)/$', views.musicant_home_page, name='musicant_home_page'),
        url(r'^list/$', views.musicants_list, name='musicants_list'),
        url(r'^detail_notice/(?P<musicant_id>[0-9]+)/$', views.detail_notice, name='detail_notice'),
]
