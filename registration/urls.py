from registration.models import *
from django.conf.urls import url
from django.views.generic import TemplateView
from registration.views import *

urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='login'),
    url(r'^user/success/', TemplateView.as_view(template_name='register/user/success.html'),
        name='user_registration_success'),
]
