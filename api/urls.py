from django.urls import path, include
from .views import GetUIDView

urlpatterns = [
    path('all/', GetUIDView.as_view(), name='list_flights')
]
