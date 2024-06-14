from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import SignupForm, SignInForm


class SignUp(FormView):
    """Create a new user."""

    template_name = "accounts/sign_up.html"
    form_class = SignupForm
    form_name = "form"
    redirect_authenticated_user = True
    success_url = reverse_lazy("sign_in")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SignIn(LoginView):
    """Login a user."""

    template_name = "accounts/sign_in.html"
    fields = ["username", "password"]
    redirect_authenticated_user = True
    authentication_form = SignInForm

    def get_success_url(self):
        return reverse_lazy("task_list")
