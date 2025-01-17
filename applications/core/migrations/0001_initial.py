# Generated by Django 5.0 on 2024-01-22 00:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'business',
                'verbose_name_plural': 'businesses',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/')),
                ('description', models.TextField(blank=True, null=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.business')),
            ],
            options={
                'verbose_name': 'company',
                'verbose_name_plural': 'companies',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Judgement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField()),
                ('vote', models.IntegerField(choices=[(-2, 'Very Bad'), (-1, 'Bad'), (0, 'Neutral'), (1, 'Good'), (2, 'Very Good')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.company')),
            ],
        ),
    ]
