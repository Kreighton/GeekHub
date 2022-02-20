# Generated by Django 4.0.1 on 2022-01-30 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parse_news', '0002_alter_news_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('by', models.CharField(default='', max_length=100, null=True)),
                ('descendants', models.CharField(default='', max_length=100, null=True)),
                ('score', models.CharField(default='', max_length=100, null=True)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(default='', null=True)),
                ('time', models.CharField(default='', max_length=100, null=True)),
                ('title', models.CharField(default='', max_length=100, null=True)),
                ('type', models.CharField(default='', max_length=100, null=True)),
                ('url', models.URLField(default='', null=True)),
                ('category_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parse_news.category')),
            ],
            options={
                'verbose_name_plural': 'Works',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('by', models.CharField(default='', max_length=100, null=True)),
                ('descendants', models.CharField(default='', max_length=100, null=True)),
                ('score', models.CharField(default='', max_length=100, null=True)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(default='', null=True)),
                ('time', models.CharField(default='', max_length=100, null=True)),
                ('title', models.CharField(default='', max_length=100, null=True)),
                ('type', models.CharField(default='', max_length=100, null=True)),
                ('url', models.URLField(default='', null=True)),
                ('category_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parse_news.category')),
            ],
            options={
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('by', models.CharField(default='', max_length=100, null=True)),
                ('descendants', models.CharField(default='', max_length=100, null=True)),
                ('score', models.CharField(default='', max_length=100, null=True)),
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(default='', null=True)),
                ('time', models.CharField(default='', max_length=100, null=True)),
                ('title', models.CharField(default='', max_length=100, null=True)),
                ('type', models.CharField(default='', max_length=100, null=True)),
                ('url', models.URLField(default='', null=True)),
                ('category_fk', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='parse_news.category')),
            ],
            options={
                'verbose_name_plural': 'Asks',
            },
        ),
    ]
