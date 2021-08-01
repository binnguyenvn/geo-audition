"""
    Base model
    with ID, creator, editor, create time. modifi time
"""

from django.contrib.auth import get_user_model
from django.db.models import CASCADE, CharField, DateTimeField, ForeignKey, Model
from django.utils import timezone

User = get_user_model()


class BaseModel(Model):
    """
    Base
    """

    time_created = DateTimeField(
        verbose_name="Created on", auto_now_add=True, null=True
    )
    time_modified = DateTimeField(
        verbose_name="Last modified on", auto_now=True, null=True
    )
    creator = ForeignKey(
        User,
        verbose_name="Created by",
        related_name="%(app_label)s_%(class)s_creator",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    last_modified_by = ForeignKey(
        User,
        verbose_name="Last modified by",
        related_name="%(app_label)s_%(class)s_last_modified",
        null=True,
        blank=True,
        on_delete=CASCADE,
    )
    creator_by_username = CharField(
        "Creator Username", max_length=255, blank=True, null=True
    )
    modified_by_username = CharField(
        "Modified Username", max_length=255, blank=True, null=True
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.time_created:
            self.time_created = timezone.now()

        self.time_modified = timezone.now()
        return super(BaseModel, self).save(*args, **kwargs)
