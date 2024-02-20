from django.contrib import admin
from .models import Article, Famille, S_famille, S_article
# Register your models here.

admin.site.register(Article)
admin.site.register(Famille)
admin.site.register(S_famille)
admin.site.register(S_article)