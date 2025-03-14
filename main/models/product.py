from django.db import models
from django.utils.text import slugify


class Filter_types(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    svg = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    parent = models.JSONField(blank=True, null=True)


    class Meta:
        verbose_name_plural = "Filter_types"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Manafacturers(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="manafacturers/", blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Manafacturers"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brands_of_equipments(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Brands_of_equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipments(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="equipments/", blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Products(models.Model):
    firm = models.ForeignKey(Manafacturers, related_name='manafacturers', on_delete=models.CASCADE,db_index=True)
    article_number = models.CharField(max_length=100, unique=True,db_index=True)
    type = models.ForeignKey(Filter_types, related_name='filter_types', on_delete=models.CASCADE,db_index=True)
    description = models.TextField(blank=True)
    specifications = models.JSONField(blank=True, null=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    slug = models.SlugField(unique=True,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.article_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firm} - {self.article_number}"
