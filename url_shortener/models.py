# -*- coding: utf-8 -*-
import random
import string

from django.db import models
from django.core.urlresolvers import reverse


class URLShortcut(models.Model):
    """
    URL and shortcut (slug)
    """
    url = models.URLField('Adres URL')
    slug = models.SlugField(u'Skrót', unique=True)

    class Meta:
        verbose_name = u'Skrót'
        verbose_name_plural = u'Skróty'

    def save(self, *args, **kwargs):
        """
        Generate slug for new objects. Saving all objects
        :param args:
        :param kwargs:
        :return:
        """
        if not self.id:
            self.slug = URLShortcut.generate_unique_slug()
        super(URLShortcut, self).save(*args, **kwargs)

    def __unicode__(self):
        return '{} ({})'.format(self.slug, self.url)

    def get_shortcut_url(self):
        """
        :return: reversed url for this shortcut (without domain name)
        """
        return reverse('shortcut', kwargs={'slug': self.slug})

    @staticmethod
    def generate_unique_slug(char_number=10):
        """
        :return: random unique code for slug (10 chars by default)
        """
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(char_number))
        if URLShortcut.objects.filter(slug=code):
            return URLShortcut.generate_unique_slug()
        return code
