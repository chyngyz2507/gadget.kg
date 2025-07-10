from django.urls import path

from user.views import RegisterUser, LoginView, LogoutView

urlpatterns = [
    path("", RegisterUser.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),

]