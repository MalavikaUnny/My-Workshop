from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from braces.views import LoginRequiredMixin, AnonymousRequiredMixin
from django.views.generic.edit import FormView, UpdateView
from registration.forms import UserRegistrationForm
from registration.models import User



def index(request):
    return HttpResponse("Hello, world. You're at the registration index.")
class Home(TemplateView):
    template_name="index.html"

class UserRegistrationView(AnonymousRequiredMixin, FormView):
    template_name = "register_user.html"

    authenticated_redirect_url = reverse_lazy(u"home")
    form_class = UserRegistrationForm
    success_url = '/register/user/success/'

    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)
