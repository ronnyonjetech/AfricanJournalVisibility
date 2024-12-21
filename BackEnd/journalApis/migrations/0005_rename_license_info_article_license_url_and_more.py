# Generated by Django 5.0 on 2024-11-14 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApis', '0004_lastprocessedjournal_article_abstract_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='license_info',
            new_name='license_url',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='end_page',
            new_name='publisher',
        ),
        migrations.RemoveField(
            model_name='article',
            name='issn',
        ),
        migrations.RemoveField(
            model_name='article',
            name='issn_electronic',
        ),
        migrations.RemoveField(
            model_name='article',
            name='issn_print',
        ),
        migrations.RemoveField(
            model_name='article',
            name='start_page',
        ),
        migrations.AddField(
            model_name='article',
            name='electronic_issn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='page_end',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='page_start',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='print_issn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='subjects',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='citation_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='articles/pdfs/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='reference_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='volume',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='journalApis.volume'),
        ),
    ]