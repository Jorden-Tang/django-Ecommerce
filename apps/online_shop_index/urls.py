from django.conf.urls import url, include
from django.contrib import admin
from . import views
from apps.online_shop_dashboard import views as view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', view.dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^log_out', views.log_out),
    url(r'^forgot_password', views.forgot_password),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    