from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .views import *

handler404 = error_page

urlpatterns = [
    path('',index,name="index"),
    path('sitemap.xml',sitemap_page,name="sitemap"),
    path('donation/', donate, name='donation'),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
