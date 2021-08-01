from factory import Faker
from factory.django import DjangoModelFactory
from ghub.services.models import Service


class ServiceFactory(DjangoModelFactory):

    name = Faker("name")
    url = Faker("url")
    description = Faker("name")

    class Meta:
        model = Service
        django_get_or_create = ["name"]
