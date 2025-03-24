from django.db import models
from django.utils.text import slugify


class SubCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    type = models.ForeignKey("Filter_types", on_delete=models.CASCADE, db_column="type_id")
    alt_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name_plural = "SubCategories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alt_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Filter_types(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    svg = models.TextField()
    subcategories = models.ManyToManyField("SubCategory", blank=True, help_text="If ")

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
    slug = models.SlugField(unique=True, null=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="manafacturers/", blank=True, null=True)

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
    slug = models.SlugField(unique=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Brands_of_equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Models_of_Brands(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    brand = models.ForeignKey(Brands_of_equipments, related_name="models", on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Models_of_Brands"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Equipments(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="equipments/", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Equipments"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Products(models.Model):
    type = models.ForeignKey(Filter_types, related_name='filter_types', on_delete=models.CASCADE,db_index=True)
    firm = models.ForeignKey(Manafacturers, related_name='manafacturers', on_delete=models.CASCADE,db_index=True)
    article_number = models.CharField(max_length=100, unique=True,db_index=True)
    slug = models.SlugField(unique=True, null=True, db_index=True)
    description = models.TextField(blank=True)
    specifications = models.JSONField(blank=True, null=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    subcategory = models.ForeignKey("SubCategory", on_delete=models.CASCADE, blank=True, null=True, help_text="If subcategories have choose it")
    model = models.ForeignKey(Models_of_Brands, on_delete=models.CASCADE,  blank=True, null=True, help_text="This is for only Brands category")
    equipment = models.ForeignKey(Equipments, on_delete=models.CASCADE,  blank=True, null=True, help_text="This is for only Equipments category")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.article_number)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.firm} - {self.article_number}"
