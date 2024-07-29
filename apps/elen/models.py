from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name


class Blog(BaseModel):
    name = models.CharField(max_length=225)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_category')
    tags = models.ManyToManyField(Tag, related_name='blog_tags', blank=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    