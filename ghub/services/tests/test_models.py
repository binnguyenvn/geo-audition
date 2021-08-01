import pytest

from ghub.services.models import Service

pytestmark = pytest.mark.django_db


def test_service_get_absolute_url(service: Service):
    assert service.get_absolute_url() == f"/api/services/{service.id}/"
