from django.urls import path
from authentication import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('signup/', views.RegisterUser.as_view(), name="register_user"),
    path('logout/', views.Logout.as_view(), name="logout_user"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/<int:id>', views.GetProfile.as_view(), name="get_profile")
]