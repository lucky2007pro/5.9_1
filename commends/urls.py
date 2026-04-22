from django.urls import path
from .views import CommendListCreateView, CommendDetailView

urlpatterns = [
    path('', CommendListCreateView.as_view(), name='commend-list'),
    path('<int:pk>/', CommendDetailView.as_view(), name='commend-detail'),
]