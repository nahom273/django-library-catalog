from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  
    path("catalog/<int:catalog_id>/", views.catalog_detail, name="catalog_detail"),
]
