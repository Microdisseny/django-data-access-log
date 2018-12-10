from django.db import models
from django.utils.translation import ugettext_lazy as _


class DataAccessLog(models.Model):
    """Model that contains all the logged information."""
    model = models.CharField('Accessed Model', max_length=100, null=False, blank=False)
    viewset = models.CharField('Accessed ViewSet', max_length=100, null=False, blank=False)
    timestamp = models.DateTimeField('Access timestamp', auto_now_add=True, editable=False, null=False, blank=False)
    user = models.CharField('User', max_length=255, null=False, blank=False)
    url = models.CharField('URL', max_length=255, null=False, blank=False)
    response = models.TextField('Response content', null=False, blank=False)

    def save(self, *args, **kwargs):
        # Only creation allowed
        if self.pk is None:
            super(DataAccessLog, self).save(*args, **kwargs)

    def __str__(self):
        return '{}@{}'.format(self.viewset, self.timestamp)

    class Meta:
        verbose_name = _('data access log')
        verbose_name_plural = _('data access logs')
