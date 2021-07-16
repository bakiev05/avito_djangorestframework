from rest_framework.routers import DefaultRouter
from categories.views import *


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='categories')


# The API URLs are now determined automatically by the router.
urlpatterns = router.urls