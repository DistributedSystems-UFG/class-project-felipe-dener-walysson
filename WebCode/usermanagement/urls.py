from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('home', views.home, name='home'),
    path('temperature', csrf_exempt(views.temperature), name='temperature'),
    path('temperatureView', views.temperature_view, name='temperatureView'),
    path('lightSensor', csrf_exempt(views.light_sensor), name='lightSensor'),
    path('lightSensorView', views.light_sensor_view, name='lightSensorView'),
    path('action', csrf_exempt(views.action), name='action'),
    path('led', csrf_exempt(views.led), name='led'),
]
