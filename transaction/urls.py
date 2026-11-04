from django.urls import path, include
from rest_framework import routers
from .views import TransactionViewSet

router = routers.SimpleRouter()

router.register(r"", TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]