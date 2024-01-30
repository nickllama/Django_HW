from django.urls import path, include
from catalog.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
]