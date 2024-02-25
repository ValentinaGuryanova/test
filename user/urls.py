from django.urls import path

from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.apps import UserConfig

app_name = UserConfig.name

urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='create_user'),

]
