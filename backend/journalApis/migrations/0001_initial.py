# Generated by Django 5.0 on 2024-08-03 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('doi', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='journalApis.journal')),
            ],
            options={
                'unique_together': {('journal', 'volume_number')},
            },
        ),
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='pdfs/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('volume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='journalApis.volume')),
            ],
        ),
    ]