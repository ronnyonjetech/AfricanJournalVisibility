# Generated by Django 5.0 on 2024-09-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApis', '0002_remove_article_article_type_remove_article_volume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='issn_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
