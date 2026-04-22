from django.urls import path
from .views import CommendView, CommendCreateView

urlpatterns = [
    path('', CommendView.as_view()),
    path('create/', CommendCreateView.as_view()),
]