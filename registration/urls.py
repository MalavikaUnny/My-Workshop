from registration.models import *
from django.conf.urls import url
from django.views.generic import TemplateView
from registration.views import *


urlpatterns = [
    url(r'^$', UserRegistrationView.as_view(), name='register_user'),
    url(r'^user/$', UserRegistrationView.as_view(), name='login'),
    url(r'^user/success/', TemplateView.as_view(template_name='register/user/success.html'),
        name='user_registration_success'),
    url(r'^chocolate/add/', AddChocolateView.as_view(), name='add_chocolate'),
    url(r'^chocolate/success/',TemplateView.as_view(template_name = 'register/chocolate/success.html'),name="success"),
    url( r'^chocolate/info/(?P<choco_id>\d+)/$', ChocolateDetailsView.as_view(), name="chocolate_info"),
    url(r'^user/profile/edit/$', UserProfileUpdateView.as_view(), name='update'),
]
