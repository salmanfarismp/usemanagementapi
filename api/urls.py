from django.urls import path
from . import views
from .views import MyTokenObtainPairView,UserTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('',views.get_routes),
    path('add/',views.add_data),
    path('usertable/',views.get_data),
    path('usertoken/', UserTokenObtainPairView.as_view(), name='user_token_obtain_pair'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('usertoken/refresh/', TokenRefreshView.as_view(), name='user_token_refresh'),
    path('users/',views.UserList.as_view()),
    path('cred/<int:pk>',views.UserDetail.as_view())
]