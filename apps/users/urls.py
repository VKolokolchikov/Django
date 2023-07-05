from rest_framework.routers import DefaultRouter

from apps.users.views import TeachersAPIView

app_name = 'users'

router = DefaultRouter()
router.register(r'teachers', TeachersAPIView, basename='teachers')

urlpatterns = router.urls
