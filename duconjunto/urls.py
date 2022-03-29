from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)