
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from accounts import urls as accounts_urls
from soMedia import urls_django_auth  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('accounts/', include(urls_django_auth)), 
    path('', include('chat.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
