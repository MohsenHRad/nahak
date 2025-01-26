from django.urls import path

from account_module import views

urlpatterns = [
    path('', views.UserEditProfile.as_view(), name='edit_profile_view'),
    path('users/', views.users_json, name='json_response_users'),
]
