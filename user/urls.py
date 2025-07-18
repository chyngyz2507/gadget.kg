from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user import views

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view()),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),
    path('activate/<int:pk>/', views.ActivateAPIView.as_view(), name='active'),
]
