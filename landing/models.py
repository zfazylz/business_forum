from django.db import models
from django.utils.translation import gettext as _


class FeedBack(models.Model):
    name = models.CharField(_('name'), max_length=200)
    email = models.EmailField(_('email'))
    message = models.TextField(_('message'), max_length=1000)
