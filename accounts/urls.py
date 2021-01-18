from django.urls import path, include
from accounts.views import *

urlpatterns = [
    path('create/', register_users, name="create"),
    path('edit/', edit_users, name="edit"),
    path('see/', view_your_user, name="see"),
]