from django.db import models
     
class Language(models.Model):
    language=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f" {self.language}"
     
class Platform(models.Model):
    platform=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f" {self.platform}"
    
class Country(models.Model):
     country=models.CharField(max_length=1000)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f" {self.country}"
     
class ThematicArea(models.Model):  
     thematic_area=models.CharField(max_length=1000)
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f" {self.thematic_area}"
     
class Journal(models.Model):
     journal_title=models.CharField(max_length=1055)
     #platform=models.ForeignKey(Platform,on_delete=models.CASCADE,unique=True,null=True, blank=True)
     platform = models.ForeignKey(Platform, on_delete=models.CASCADE, null=True, blank=True)
     #country=models.ForeignKey(Country,on_delete=models.CASCADE,unique=True,null=True, blank=True)
     country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True, blank=True)
     publishers_name=models.CharField(max_length=1055,null=True, blank=True)
     #language=models.ForeignKey(Language,on_delete=models.CASCADE,unique=True,null=True, blank=True)
     language=models.ForeignKey(Language,on_delete=models.CASCADE,null=True, blank=True)
     #thematic_area=models.ForeignKey(ThematicArea,on_delete=models.CASCADE,unique=True,null=True, blank=True)
     thematic_area=models.ForeignKey(ThematicArea,on_delete=models.CASCADE,null=True, blank=True)
     issn_number=models.CharField(max_length=100, null=True, blank=True)
    #  link = models.URLField(max_length=2048, blank=True, null=True)
     link = models.TextField(blank=True, null=True)
     aim_identifier = models.BooleanField(blank=True, null=True)
     medline=models.BooleanField(blank=True, null=True)
     google_scholar_index=models.BooleanField(blank=True, null=True)
     impact_factor=models.IntegerField(blank=True, null=True)
     sjr=models.BooleanField(blank=True, null=True)
     h_index=models.IntegerField(blank=True, null=True)
     eigen_factor=models.BooleanField(blank=True, null=True)
     eigen_metrix=models.CharField(max_length=1055,null=True, blank=True)
     snip=models.BooleanField(blank=True, null=True)
     snip_metrix=models.FloatField(blank=True, null=True)
     open_access_journal=models.BooleanField(blank=True, null=True)
     listed_in_doaj=models.BooleanField(blank=True, null=True)
     present_issn=models.BooleanField(blank=True, null=True)
     publisher_in_cope=models.BooleanField(blank=True, null=True)
     online_publisher_africa=models.BooleanField(blank=True, null=True)
     hosted_on_inasps=models.BooleanField(blank=True, null=True)
     summary = models.TextField(null=True, blank=True)

     def __str__(self):
        return f"{self.id}-{self.journal_title}"


class JournalImage(models.Model):
    journal = models.OneToOneField(Journal, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to='journals/images/', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)  # Optional description of the image
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.journal.journal_title} uploaded on {self.uploaded_at}"


class Volume(models.Model):
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, related_name="volumes")
    volume_number = models.PositiveIntegerField(verbose_name="Volume Number")
    issue_number = models.PositiveIntegerField(verbose_name="Issue Number", default=1)  # New field for issue number
    year = models.PositiveIntegerField(verbose_name="Year of Publication")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['journal', 'volume_number', 'issue_number'], name='unique_journal_volume_issue')
        ]

    def __str__(self):
        return f"Volume {self.volume_number} No. {self.issue_number} of {self.journal.journal_title} ({self.year})"

class Article(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name="articles", blank=True)  
    title = models.CharField(max_length=255)
    authors = models.TextField()  # Store a list of authors as a comma-separated string
    keywords = models.TextField()
    publication_date = models.DateField()
    pdf = models.FileField(upload_to='articles/pdfs/', blank=True, null=True)
    
    def __str__(self):
        return self.title

