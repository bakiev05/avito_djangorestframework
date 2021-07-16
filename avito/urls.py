# from django.urls import include, path
# from rest_framework import routers
# from posts import views
# from django.contrib import admin

# router = routers.DefaultRouter()
# # router.register(r'users', views.UserViewSet)


# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
# from posts.views import api_roots


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('categories/',include('categories.urls')),
    path('users/',include('users.urls')),
    path('comments/',include('comments.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
