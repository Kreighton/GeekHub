from django.db import models


class Category(models.Model):
    cus_cat = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.cus_cat



class News(models.Model):
    category_fk = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)

    by = models.CharField(max_length=100, default='', null=True)
    descendants = models.CharField(max_length=100, default='', null=True)
    score = models.CharField(max_length=100, default='', null=True)
    id = models.IntegerField(default=0, null=False, primary_key=True, unique=True)
    text = models.TextField(default='', null=True)
    time = models.CharField(max_length=100, default='', null=True)
    title = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=100, default='', null=True)
    url = models.URLField(default='', null=True)

    class Meta:
        verbose_name_plural = 'News'


class Work(models.Model):
    category_fk = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)

    by = models.CharField(max_length=100, default='', null=True)
    descendants = models.CharField(max_length=100, default='', null=True)
    score = models.CharField(max_length=100, default='', null=True)
    id = models.IntegerField(default=0, null=False, primary_key=True, unique=True)
    text = models.TextField(default='', null=True)
    time = models.CharField(max_length=100, default='', null=True)
    title = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=100, default='', null=True)
    url = models.URLField(default='', null=True)

    class Meta:
        verbose_name_plural = 'Shows'


class Job(models.Model):
    category_fk = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)

    by = models.CharField(max_length=100, default='', null=True)
    descendants = models.CharField(max_length=100, default='', null=True)
    score = models.CharField(max_length=100, default='', null=True)
    id = models.IntegerField(default=0, null=False, primary_key=True, unique=True)
    text = models.TextField(default='', null=True)
    time = models.CharField(max_length=100, default='', null=True)
    title = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=100, default='', null=True)
    url = models.URLField(default='', null=True)

    class Meta:
        verbose_name_plural = 'Jobs'


class Ask(models.Model):
    category_fk = models.ForeignKey('Category', on_delete=models.CASCADE, default=None, null=True)

    by = models.CharField(max_length=100, default='', null=True)
    descendants = models.CharField(max_length=100, default='', null=True)
    score = models.CharField(max_length=100, default='', null=True)
    id = models.IntegerField(default=0, null=False, primary_key=True, unique=True)
    text = models.TextField(default='', null=True)
    time = models.CharField(max_length=100, default='', null=True)
    title = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=100, default='', null=True)
    url = models.URLField(default='', null=True)

    class Meta:
        verbose_name_plural = 'Asks'