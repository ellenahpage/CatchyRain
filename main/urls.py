from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('whyRWH', views.whyRWH, name='whyRWH')
    # path('', views.contact, name='contact'),
    # path('', views.documentation, name='documentation'),
    # path('', views.usermanual, name='usermanual')
]
