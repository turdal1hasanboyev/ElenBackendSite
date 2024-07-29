from django.db import models

from apps.common.models import BaseModel

from ckeditor.fields import RichTextField


class GetInTouch(BaseModel):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225, null=True, blank=True)
    message = RichTextField(null=True, blank=True)
    subject = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    