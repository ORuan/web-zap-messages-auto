from django.urls import path, include
from seln.views import *

urlpatterns = [
    path('panel/', panel, name="panel"),
    path('qr-code-read/', read_qr_code, name="panel"),
]