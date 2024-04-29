from django.urls import path
from CBV import views

app_name = 'CBV'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('index',views.IndexView.as_view(),name='index'),
    path('school_list',views.SchoolListView.as_view(),name='school_list'),
    path('<int:pk>',views.SchoolDetailView.as_view(),name='school_detail'),
    path('create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='school_update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='school_delete'),

]
