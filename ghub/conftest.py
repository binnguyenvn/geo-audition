import pytest

from ghub.services.models import Service
from ghub.services.tests.factories import ServiceFactory
from ghub.users.models import User
from ghub.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def service() -> Service:
    return ServiceFactory()
