from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import SavePoint


urlpatterns = [
    path('save_point/', SavePoint.as_view(), name='save_point')
]
