
from django.contrib import admin

# from .models import Volume,Article,ArticleType


# admin.site.register(Article)
# admin.site.register(Volume)
# admin.site.register(ArticleType)

from .models import *

admin.site.register(Language)
admin.site.register(Platform)
admin.site.register(Country)
admin.site.register(Journal)
admin.site.register(ThematicArea)
admin.site.register(Article)
admin.site.register(Volume)
admin.site.register(ArticleType)
