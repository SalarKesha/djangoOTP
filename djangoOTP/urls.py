from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from demo.views import UserListAPI, LoginAPI, ProfileAPI, ApiToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserListAPI.as_view(), name='user_list'),
    path('api/token/', ApiToken.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileAPI.as_view(), name='profile'),
]
