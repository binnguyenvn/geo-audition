from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from ghub.users.api.views import UserViewSet
from ghub.services.api.views import ServiceViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("services", ServiceViewSet)


app_name = "api"
urlpatterns = router.urls
