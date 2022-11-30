from .views import *
from django.urls import path

urlpatterns = [
    path('category/', CategoryCreateList.as_view()),
    path('product/', ProductCreateList.as_view()),
    # path('billing/', BillingCreateList.as_view()),
    path('category/<int:pk>/', CategoryUpdateDelete.as_view()),
    path('product/<int:pk>/', ProductUpdateDeleteFilter.as_view()),
    path('cart/', CartCreateList.as_view()),
    path('cart/<int:pk>/', CartDetail.as_view()),
    path('store/', StoreCreateList.as_view()),
    
    
]