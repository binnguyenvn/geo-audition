import pytest
from django.test import RequestFactory

from ghub.services.api.views import ServiceViewSet
from ghub.services.models import Service

pytestmark = pytest.mark.django_db


class TestServiceViewSet:
    def test_get_queryset(self, service: Service, rf: RequestFactory):
        view = ServiceViewSet()
        request = rf.get("/fake-url/")
        view.request = request
        assert service in view.get_queryset()
