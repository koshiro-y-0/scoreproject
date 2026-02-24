from django.urls import path
from . import views

app_name = 'omb'

urlpatterns = [
    path('', views.IndexView.as_view(), name='top'),
    path('list/', views.OmbListView.as_view(), name='list'),
    path('post/', views.OmbCreateView.as_view(), name='post'),
]