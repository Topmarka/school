from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('crm/', include('management.urls')),
    path('api/', include('mainapp.api.urls')),
    path('api/management/', include('management.api.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
