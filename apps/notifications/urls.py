from django.urls import path

from apps.notifications.views import NotificationAPIView

app_name = 'notifications'

urlpatterns = [
    path('notifications/', NotificationAPIView.as_view(), name='notifications'),
]
