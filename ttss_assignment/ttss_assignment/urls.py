from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('base.urls')),
    path('votes/', include('votes.urls')),
    path('', include('pages.urls')),
]
