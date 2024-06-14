from django.urls import path
from .views import SignUp, SignIn

urlpatterns = [
    path("sign-up", SignUp.as_view(), name="sign_up"),
    path("sign-in", SignIn.as_view(), name="sign_in"),
]
