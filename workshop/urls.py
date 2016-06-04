from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.views import Home
from registration.urls import *
from workshop.views import *
from django.views.generic import TemplateView
from registration import urls as reg_urls
from django.contrib.auth import views as auth_views



admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'workshop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^user/login/$', anonymous_required(auth_views.login),{'template_name': 'login.html'},name='login'),
    url(r'^$', Home.as_view(), name='home'),
    url(r'^register/', include('registration.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^solution/create/success/$', TemplateView.as_view(template_name="solutions/solution_create_success.html"), name='solution_create_success'),
    url(r'^contact/', TemplateView.as_view(template_name="register/contact_us.html"), name='contact_us'),
    url(r'^register/', include(reg_urls), name='register'),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'register/login.html'},
        name='login'),
    url(r'^user/logout/$',
        auth_views.logout,
        {'template_name': 'register/logout.html'},
        name='logout'),
    url(r'^password/change/$',
        auth_views.password_change,
        {'template_name': 'register/passwd_change.html'},
        name='password_change'),
    url(r'^password_change/done/$',
        auth_views.password_change_done,
        {'template_name': 'register/password_change_done.html'},
        name='password_change_done'),
    url(r'^password/reset/$',
        anonymous_required(auth_views.password_reset),
        {'template_name': 'register/passwd_reset.html',
        'email_template_name':'register/passwd_reset_email.html'},
        name='password_reset'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        anonymous_required(auth_views.password_reset_confirm),
        {'template_name': 'register/passwd_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^password/reset/complete/$', anonymous_required(auth_views.password_reset_complete),
        {'template_name': 'register/passwd_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^password/reset/done/$',
        anonymous_required(auth_views.password_reset_done),
        {'template_name': 'register/passwd_reset_done.html'},
        name='password_reset_done'),
]
