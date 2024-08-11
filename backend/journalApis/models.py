from django.db import models

class Volume(models.Model):
    volume_number = models.PositiveIntegerField(unique=True, verbose_name="Volume Number")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Volume {self.volume_number}"
    

class ArticleType(models.Model):
     article_type = models.CharField(max_length=255)
     created_at = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f" {self.article_type}"
    
     
class Article(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE, related_name="articles")
    article_type=models.ForeignKey(ArticleType,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    authors = models.TextField()  # Store a list of authors as a comma-separated string
    keywords = models.TextField()
    publication_date = models.DateField()
   
    #publication_details = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

