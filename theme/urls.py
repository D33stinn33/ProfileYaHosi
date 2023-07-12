from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name="home"),
]