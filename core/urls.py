from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'core'

# Router para ViewSets da API REST
router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]