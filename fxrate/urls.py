from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from fxrate.views import Homepage

urlpatterns = i18n_patterns(
    path('blog/', include('blog.urls')),
    path('exchange/', include('exchange.urls')),
    path('', Homepage.as_view(), name="homepage"),
    path('admin/', admin.site.urls),
    prefix_default_language=False
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
