# Generated by Django 5.0 on 2024-10-13 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThematicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thematic_area', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journal_title', models.CharField(max_length=1055)),
                ('publishers_name', models.CharField(blank=True, max_length=1055, null=True)),
                ('issn_number', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('aim_identifier', models.BooleanField(blank=True, null=True)),
                ('medline', models.BooleanField(blank=True, null=True)),
                ('google_scholar_index', models.BooleanField(blank=True, null=True)),
                ('impact_factor', models.IntegerField(blank=True, null=True)),
                ('sjr', models.BooleanField(blank=True, null=True)),
                ('h_index', models.IntegerField(blank=True, null=True)),
                ('eigen_factor', models.BooleanField(blank=True, null=True)),
                ('eigen_metrix', models.CharField(blank=True, max_length=1055, null=True)),
                ('snip', models.BooleanField(blank=True, null=True)),
                ('snip_metrix', models.FloatField(blank=True, null=True)),
                ('open_access_journal', models.BooleanField(blank=True, null=True)),
                ('listed_in_doaj', models.BooleanField(blank=True, null=True)),
                ('present_issn', models.BooleanField(blank=True, null=True)),
                ('publisher_in_cope', models.BooleanField(blank=True, null=True)),
                ('online_publisher_africa', models.BooleanField(blank=True, null=True)),
                ('hosted_on_inasps', models.BooleanField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journalApis.country')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journalApis.language')),
                ('platform', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journalApis.platform')),
                ('thematic_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journalApis.thematicarea')),
            ],
        ),
        migrations.CreateModel(
            name='JournalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='journals/images/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='journalApis.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_number', models.PositiveIntegerField(verbose_name='Volume Number')),
                ('issue_number', models.PositiveIntegerField(default=1, verbose_name='Issue Number')),
                ('year', models.PositiveIntegerField(verbose_name='Year of Publication')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volumes', to='journalApis.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.TextField()),
                ('keywords', models.TextField()),
                ('publication_date', models.DateField()),
                ('pdf', models.FileField(blank=True, null=True, upload_to='articles/pdfs/')),
                ('volume', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='journalApis.volume')),
            ],
        ),
        migrations.AddConstraint(
            model_name='volume',
            constraint=models.UniqueConstraint(fields=('journal', 'volume_number', 'issue_number'), name='unique_journal_volume_issue'),
        ),
    ]
