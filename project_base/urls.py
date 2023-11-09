from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_web.urls')),
    path('my/',include('app_blog.urls')),
]
