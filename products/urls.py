from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.product_list, name='product_search'),
]
