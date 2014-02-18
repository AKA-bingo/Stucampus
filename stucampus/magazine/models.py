#-*- coding: utf-8
from django.db import models
from django.contrib.auth.models import User

from stucampus.custom.models_utils import file_save_path


def save_path(instance, filename):
    return os.path.join(instance.name, filename)


class Magazine(models.Model):

    class Meta:
        permissions = (
            ('magazine_add', u'添加杂志'),
            ('magazine_modify', u'编辑杂志'),
            )

    name = models.CharField(max_length=30)
    title = models.CharField(max_length=40)
    issue = models.IntegerField(unique=True)
    summary = models.CharField(max_length=300, null=True, blank=True)
    pdf_file = models.FileField(upload_to=save_path, null=True, blank=True)

    create_date = models.DateField(auto_now_add=True)
    modify_date = models.DateField(auto_now=True)
