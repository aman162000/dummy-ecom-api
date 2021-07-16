from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from .views import index, handler404_page

handler404 = handler404_page

urlpatterns = [
    path('',index,name="index"),
    path('admin/', admin.site.urls),
    path('s/', handler404_page, name='404'),
    path('api/',include('api.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
