from django.urls import path
from . import views

app_name = 'score'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('in-score/', views.InScoreView.as_view(), name='in-score'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'), 
    path('detail/', views.SubjectDetailView.as_view(), name='detail'),
    path('subject/<int:pk>/', views.SubjectScoreListView.as_view(), name='subject_detail'),
]