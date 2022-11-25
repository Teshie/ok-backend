from django.urls import path, include
from . import views


urlpatterns = [
    path("signup", views.CreateProfile.as_view(), name='signup'),
    path("login", views.LoginViewSet.as_view(), name='login'),
    path("get-user-types", views.get_user_types, name="get_user_types"),
    path("list-accounts", views.AccountList.as_view(), name="list_accounts"),
   
]
