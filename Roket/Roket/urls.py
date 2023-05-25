from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.views import *
from django.conf.urls import handler404 , handler500


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
    re_path(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    re_path('', include(('pages.urls','pages'), namespace='pages')),
    re_path('ckeditor/', include('ckeditor_uploader.urls')),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'pages.views.error404'
handler500 = 'pages.views.error500'