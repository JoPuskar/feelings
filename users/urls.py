from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views
from .views import LogoutView

urlpatterns = [
    url(r'^dashboard/$', views.Dashboard.as_view(), name='dashboard'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    url('^', include('django.contrib.auth.urls')),
]