from django.urls import path, include
from . import views


urlpatterns = [
    path("signup", views.CreateProfile.as_view(), name='signup'),
    path("login", views.LoginViewSet.as_view(), name='login'),
    path("get-client-types", views.get_client_types, name="get_client_types"),
   
]
