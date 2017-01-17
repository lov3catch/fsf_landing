import os
from random import choice
from string import ascii_letters

from django.contrib.sites.models import Site
from django.db import models


def unique_code(length=10):
    return ''.join(choice(ascii_letters) for i in range(length))


class Area(models.Model):
    site = models.OneToOneField(Site, related_name='area', verbose_name="сайт")
    chance = models.IntegerField(default=100, verbose_name='шанс')
    template_path = models.CharField(default='master', max_length=10, verbose_name='папка с шаблонами')
    is_secure = models.BooleanField(default=False, verbose_name='https')

    def get_template(self, path):
        return os.path.join(self.template_path, path)

    def get_url(self):
        return '://'.join(['https' if self.is_secure else 'http', self.site.domain])

    @staticmethod
    def get_random():
        result = list(map(lambda i: [i] * i.chance, Area.objects.all()))
        return choice([item for sublist in result for item in sublist])

    def __str__(self):
        return self.site.name


class Visitor(models.Model):
    area = models.ForeignKey(Area, verbose_name='площадка')
    campaign = models.ForeignKey('Campaign', verbose_name='компания', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Partner(models.Model):
    title = models.CharField(verbose_name='название', max_length=50)
    description = models.CharField(verbose_name='описание', max_length=500)


class Campaign(models.Model):
    title = models.CharField(verbose_name='название', max_length=50)
    description = models.CharField(verbose_name='описание', max_length=500)
    short_url = models.URLField(verbose_name='ссылка')
    partner = models.ForeignKey(Partner, verbose_name='партнёр')


class Order(models.Model):
    visitor = models.ForeignKey(Visitor)
    phone = models.CharField(max_length=15, verbose_name='номер телефона')
    message = models.TextField(verbose_name='текст сообщения')
    is_available = models.BooleanField(default=False, verbose_name='доступен для обработки менеджером')
    send_to_manager = models.DateTimeField(blank=True, null=True, verbose_name='дата просмотра менеджером')
    send_to_moderator = models.DateTimeField(blank=True, null=True, verbose_name='дата просмотра модератором')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Manager(models.Model):
    username = models.CharField(max_length=50, verbose_name='имя менеджера')
    code = models.CharField(max_length=10, default=unique_code, verbose_name='код')
    chanel = models.CharField(max_length=30, verbose_name='номер канала', null=True, blank=True)


class Moderator(models.Model):
    username = models.CharField(max_length=50, verbose_name='имя модератора')
    code = models.CharField(max_length=10, default=unique_code, verbose_name='код')
    chanel = models.CharField(max_length=30, verbose_name='номер канала', null=True, blank=True)
