import uuid
from pathlib import Path

from django.core.validators import FileExtensionValidator
from django.db import models


def generate_uploaded_img_name(instance, filename):
    ext = Path(filename).suffix
    new_name = f'{uuid.uuid4()}{ext}'
    return f'imgs/ongs/{new_name}'


# Create your models here.
class Ongs(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    short_name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    slogan = models.TextField(blank=True, null=True)
    img = models.ImageField(
        upload_to=generate_uploaded_img_name,
        validators=[
            FileExtensionValidator(['jpeg', 'jpg', 'png', 'webp'])
        ]
    )
    about = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return self.short_name

    class Meta:
        db_table = 'ong'
        verbose_name = 'Ong'
        verbose_name_plural = 'Ongs'
        ordering = ['name']