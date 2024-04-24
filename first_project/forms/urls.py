from django.urls import path
from forms import views

app_name = 'forms'

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("form_page/", views.form, name="forms"),
    path("users/", views.users, name="users"),
    path("base/", views.base, name="base"),
    path('user_login/', views.user_login, name='user_login'),
    path("registration/", views.registration, name="registration"),
    path("user_logout/", views.user_logout, name="user_logout"),
]
