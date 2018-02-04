from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.poll, name='poll'),
    path('<str:response>', views.poll_response, name='poll response')
]
