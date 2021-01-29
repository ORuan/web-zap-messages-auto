from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('accounts.urls', 'accounts'), namespace='users')),
    path('bot-config/', include(('seln.urls', 'seln'), namespace='seln')),
]
