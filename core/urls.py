from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/?', admin.site.urls),
    path('api/v1/', include('apps.cars.api.urls')),
    path('api/v1/', include('apps.clients.api.urls')),
    path('api/v1/', include('apps.services.api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)