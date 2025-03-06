from django.db import models
from django.utils.text import slugify

class Filter_type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = "Filter_types"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (Subcategory of {self.parent.name})" if self.parent else self.name


class Manafacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="manafacturers/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Manafacturers"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Brands_of_equipment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Brands_of_equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="equipments/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Oil_filter(models.Model):
    firm = models.ForeignKey(Manafacturer, related_name='manafacturers', on_delete=models.CASCADE)
    article_number = models.CharField(max_length=100, unique=True)
    type = models.ForeignKey(Filter_type, related_name='filter_types', on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    bp_opening_dp = models.FloatField(help_text="БПВ открытие ДП (фунтов на квадратный дюйм)")
    inner_gasket_diameter = models.FloatField(help_text="Внутренний диаметр прокладки (дюймы)")
    largest_od = models.FloatField(help_text="Крупнейший OD (дюймы)")
    efficiency = models.IntegerField(help_text="Эффективность (%)")
    gasket_hd = models.FloatField(help_text="Прокладка НД (дюймы)")
    length = models.FloatField(help_text="Длина (дюймы)")
    outer_seam_diameter = models.FloatField(help_text="Внешний Диаметр Шва (дюймы)")
    stock = models.PositiveIntegerField(default=0)

    image = models.ImageField(upload_to="oil_filters/", blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.article_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firm} - {self.article_number}"
