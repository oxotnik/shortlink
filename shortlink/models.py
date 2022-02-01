from django.db import models
from django.urls import reverse


class ShortLinks(models.Model):
    """ Таблицы сокращенные линков """
    date_create = models.DateTimeField("Дата создания", default=None)
    date_expiry = models.DateTimeField("Дата действия ссылки", null=True, blank=True)
    url = models.CharField("Ссылка",max_length=255, default=None)
    short_id = models.CharField("Ссылка ид", max_length=25, unique=True, default=None)
    short_url = models.CharField("Сокращенная ссылка", max_length=255, unique=True, default=None)
    description = models.TextField("Описание", null=True, default=None)
    is_archive = models.BooleanField("Архивная?", default=False)

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('view_link', args=[self.short_id])

