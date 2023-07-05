from django.urls import path

from apps.contacts.views import ContactsAPIView


app_name = 'contacts'


urlpatterns = [
    path('contacts/', ContactsAPIView.as_view(), name='contacts'),
]
