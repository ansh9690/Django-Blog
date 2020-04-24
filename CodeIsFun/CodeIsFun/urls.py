from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'CodeIsFun Admin'
admin.site.site_title = 'Admin Pannel'
admin.site.index_title = 'Features Area'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
]
