# Generated by Django 5.0 on 2024-12-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApis', '0013_journalswithoutarticles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=2000, null=True)),
                ('email', models.CharField(blank=True, max_length=2000, null=True)),
                ('question', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
