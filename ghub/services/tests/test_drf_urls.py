import pytest
from django.urls import resolve, reverse

from ghub.services.models import Service

pytestmark = pytest.mark.django_db


def test_service_detail(service: Service):
    assert (
        reverse("api:service-detail", kwargs={"pk": service.id})
        == f"/api/services/{service.id}/"
    )
    assert resolve(f"/api/services/{service.id}/").view_name == "api:service-detail"


def test_service_list():
    assert reverse("api:service-list") == "/api/services/"
    assert resolve("/api/services/").view_name == "api:service-list"

