# Generated by Django 5.2.4 on 2025-07-23 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subcat', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('projectdate', models.DateField(auto_now_add=True)),
                ('desc', models.TextField(default='')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('finishdatetime', models.DateTimeField()),
                ('payment', models.IntegerField()),
                ('paymentReceived', models.FloatField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Project.projectcategorymodel')),
            ],
        ),
    ]
