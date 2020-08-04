from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from fxrate.views import Homepage

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('exchange/', include('exchange.urls')),
    path('', Homepage.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
