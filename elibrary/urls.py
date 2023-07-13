
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = ([
    path("admin/", admin.site.urls),
    path("", include("app.urls", namespace="app")),
    path('accounts/', include('registration.backends.default.urls')),
]
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)