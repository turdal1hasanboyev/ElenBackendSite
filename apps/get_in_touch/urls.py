from django.urls import path

from apps.get_in_touch.views import get_in_touch


urlpatterns = [
    path('contact/', get_in_touch, name='contact'),
]
