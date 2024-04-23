from django.urls import path
from forms import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("form_page/", views.form, name="forms"),
]
