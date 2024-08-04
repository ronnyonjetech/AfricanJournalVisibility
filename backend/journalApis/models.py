from django.db import models

# Create your models here.

class Journal(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    doi = models.CharField(max_length=255, unique=True)  # Digital Object Identifier (DOI)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Volume(models.Model):
    journal = models.ForeignKey(Journal, related_name='volumes', on_delete=models.CASCADE)
    volume_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('journal', 'volume_number')  # Unique constraint per journal and volume number

    def __str__(self):
        return f"Volume {self.volume_number} - {self.journal.name}"


class PDF(models.Model):
    volume = models.ForeignKey(Volume, related_name='pdfs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
