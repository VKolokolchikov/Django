from django.urls import path

from apps.comments.views import CommentsAPIView

app_name ='comments'


urlpatterns = [
    path('comments/', CommentsAPIView.as_view(), name='comments'),
]
