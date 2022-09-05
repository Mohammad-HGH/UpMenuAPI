
from django.urls import path

# from rest_framework_simplejwt.views import TokenRefreshView

from .views import Register, Login

app_name = "user"

urlpatterns = [
    path("login/", Login.as_view(), name="token_obtain_pair"),
    path("register/", Register.as_view(), name="token_obtain_pair"),
    # path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
