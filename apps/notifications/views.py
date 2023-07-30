from rest_framework.generics import CreateAPIView
from rest_framework.throttling import AnonRateThrottle

from apps.notifications.serializers import NotificationSerializer


class NotificationThrottle(AnonRateThrottle):
    scope = 'post_anon'
    THROTTLE_RATES = {'post_anon': '3/min'}


class NotificationAPIView(CreateAPIView):
    serializer_class = NotificationSerializer
    throttle_classes = [NotificationThrottle]
