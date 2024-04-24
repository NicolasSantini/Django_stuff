from django.urls import path
from forms import views

app_name = 'forms'

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("form_page/", views.form, name="forms"),
    path("users/", views.users, name="users"),
]
