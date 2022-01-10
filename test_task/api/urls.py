from django.urls import path
from api.views import success_activate, reject_activate

app_name = 'api'

urlpatterns = [
    path('success/activated/', success_activate, name='success_activated'),
    path('reject/deactivated/', reject_activate, name='reject_deactivated')
]