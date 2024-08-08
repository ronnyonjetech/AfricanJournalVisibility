
from django.contrib import admin

from .models import Volume,Article,ArticleType


admin.site.register(Article)
admin.site.register(Volume)
admin.site.register(ArticleType)