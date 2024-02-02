"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# from catalog.views import product_detail, categories, category_products, index
#
# app_name = 'catalog'
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index, name='index'),
#     path('categories/', categories, name='categories'),
#     path('', include('catalog.urls', namespace='catalog')),
#     path('catalog/<int:pk>', category_products, name='category_products'),
#     path('product/<int:product_id>/', product_detail, name='product_detail'),
#
#
#
#
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# my_project/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from catalog.views import product_detail, categories, category_products, index

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
    # path('catalog/', include('catalog.urls', namespace='catalog')),
    path('catalog/<int:pk>/', category_products, name='category_products'),
    path('catalog/', include('catalog.urls')),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

