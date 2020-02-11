from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^show/(?P<product_id>\d+)$', views.show_product),
    url(r'^create$', views.create_product),
    url(r'^add_to_cart/(?P<product_id>\d+)$', views.add_to_cart),
    url(r'^remove_from_cart/(?P<product_id>\d+)$', views.remove_from_cart),
    url(r'^shopping_cart$', views.show_shopping_cart),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)