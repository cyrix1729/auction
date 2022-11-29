from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('login/', include('login.urls')),
    path('item/', include('item.urls')),
    path('listings/', include('listings.urls')),
    path('profile/', include('profile.urls')),
    path('list/', include('list.urls')),

    path('admin/', admin.site.urls),
]