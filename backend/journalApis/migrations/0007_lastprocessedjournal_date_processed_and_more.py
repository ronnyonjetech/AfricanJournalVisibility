# Generated by Django 5.0 on 2024-11-14 10:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApis', '0006_alter_article_license_url_alter_article_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastprocessedjournal',
            name='date_processed',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='lastprocessedjournal',
            unique_together={('last_processed_id',)},
        ),
    ]
