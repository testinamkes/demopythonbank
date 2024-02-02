from django.db import models
from django.urls import reverse

class District(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='district', blank=True)
    wikipedia_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def get_url(self):
        return reverse('bankapp:branch_by_district', args=[self.slug])

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=225, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    review = models.TextField(blank=True)
    timing = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='branch', blank=True)
    service = models.TextField(blank=True)
    faq = models.TextField(blank=True)
    testimonials = models.TextField(blank=True)
    loan_price = models.DecimalField(max_digits=10, decimal_places=2)
    available_loan = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return self.name
