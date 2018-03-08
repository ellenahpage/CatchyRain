from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    path('assumptions', views.assumptions, name='assumptions'),
    path('hardwarecomparison', views.hardwarecomparison, name='hardwarecomparison'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('rain_data', views.rain_data, name='rain_data')

    # path('', views.contact, name='contact'),
    # path('', views.documentation, name='documentation'),
    # path('', views.usermanual, name='usermanual')
]
