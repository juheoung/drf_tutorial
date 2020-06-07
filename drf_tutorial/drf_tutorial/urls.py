from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
]
