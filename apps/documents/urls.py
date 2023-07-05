from django.urls import path

from apps.documents.views import DocumentsListAPIView

app_name = 'documents'

urlpatterns = [
    path('documents/', DocumentsListAPIView.as_view(), name='documents'),
]
