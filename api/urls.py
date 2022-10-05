from django.urls import path, include
from . import views

urlpatterns = [
    path('google/callback/', views.GoogleCallbackHandler.as_view(), name='google-callback')
]