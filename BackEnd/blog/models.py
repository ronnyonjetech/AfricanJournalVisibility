from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(
        max_length=255, unique=True, help_text="Title of the blog"
    )
    blog_link = models.URLField(
        blank=True, null=True, help_text="Optional: Link to read the full blog"
    )
    description = models.TextField(
        blank=True, null=True, help_text="Detailed description of the blog"
    )
    date_published = models.DateField(
        blank=True, null=True, help_text="Date when the blog was published"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
