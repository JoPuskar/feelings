from django.conf.urls import url, include

from .views import CompanyCreateView

urlpatterns = [
    url(r'^company/create/$', CompanyCreateView.as_view(), name='create_company')
]