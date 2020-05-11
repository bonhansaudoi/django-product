from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'BNSD Admin'
admin.site.site_title = 'BNSD Admin Pannel'
admin.site.index_title = 'Welcome to BNSD Admin'

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/users/', include('accounts.urls')),	
    path('', include('layouts.urls')),
    path('article/', include('blog.urls')),


    path('oauth/', include('social_django.urls', namespace='social')), 
    path('summernote/', include('django_summernote.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 