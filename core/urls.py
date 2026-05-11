from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from ongs.views import HomeView

admin.site.site_header = 'SustentAgro'
admin.site.site_title = 'SustentAgro'
admin.site.index_title = 'Bem vindo!'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name='index'),
    path('ongs/', include('ongs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
