from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path("", views.index, name="index"),
    path('index', views.index, name='index'),
    path('help', views.help, name='help'),
    path('webpages', views.webpages, name='webpages'),
    path('users', views.users, name='users'),
]
