from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from decimal import *
from django.template.defaultfilters import slugify
from django.conf import settings

# Create your models here.

class Affiliate(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField(max_length=200)
    freebet = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)        
        super(Affiliate, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Summary(models.Model):
    name = models.CharField(max_length=30, default='', blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('view_summary', args=[self.id])

    @staticmethod
    def create_new():
        summary = Summary.objects.create()
        [Item.objects.create(affiliate=aff, summary=summary) for aff in Affiliate.objects.all()]
        return summary

    def __str__(self):
        if self.name:
            return self.name
        else:
            return 'Summary ' + str(self.id)
    
    class Meta:
        verbose_name_plural = 'Summaries'

class Item(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    summary = models.ForeignKey(Summary, on_delete=models.CASCADE)

    username = models.CharField(max_length=200, default='', blank=True)
    status = models.CharField(max_length=30, default='signup',
                              choices=[('signup', 'signup'), ('deposit', 'deposit'),
                                       ('initial', 'initial'), ('free', 'free'), ('complete', 'complete')])
    balance = models.DecimalField(default=Decimal('0.00'), max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    profit = models.DecimalField(default=Decimal('0.00'), max_digits=6, decimal_places=2)
    banked = models.BooleanField(default=False)
    

    class Meta:
        unique_together = ('affiliate', 'summary')

    def __str__(self):
        return self.affiliate.name

class Click(models.Model):
    affiliate = models.ForeignKey(Affiliate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
