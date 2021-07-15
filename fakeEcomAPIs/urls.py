from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import index
urlpatterns = [
    path('',index,name="index"),
    path('admin/', admin.site.urls),
    path('api/',include('api.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)