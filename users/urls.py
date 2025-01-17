from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", views.UserViewList.as_view(), name="register"),
    path("user_list/", views.UserViewList.as_view(), name="user_list"),
    path("user_update/<int:pk>/", views.UserViewDetails.as_view(), name="user_update"),
    path("user_delete/<int:pk>/", views.UserViewDetails.as_view(), name="user_delete"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
