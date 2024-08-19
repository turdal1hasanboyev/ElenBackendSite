from django.urls import path

from .views import home, photography, fashion, travel


urlpatterns = [
    path('', home, name='home'),
    path('photography/', photography, name='photography'),
    path('fashion/', fashion, name='fashion'),
    path('travel/', travel, name='travel'),
]
