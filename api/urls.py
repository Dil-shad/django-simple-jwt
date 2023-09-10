
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)





urlpatterns = [

    path('register',RegisterView.as_view()),
    path('login',LoginView.as_view()),
    path("api/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
]
