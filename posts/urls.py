from rest_framework.routers import DefaultRouter
from posts.views import *


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')



# The API URLs are now determined automatically by the router.
urlpatterns = router.urls