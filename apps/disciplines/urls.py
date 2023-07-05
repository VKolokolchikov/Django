from rest_framework.routers import DefaultRouter

from apps.disciplines.views import DisciplinesAPIView

app_name = 'disciplines'

router = DefaultRouter()
router.register(r'disciplines', DisciplinesAPIView, basename='disciplines')

urlpatterns = router.urls
