from django.contrib import admin
from data.models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass

class ExperienceAdmin(admin.ModelAdmin):
    pass

class ExperienceSARAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ExperienceSAR, ExperienceSARAdmin)
admin.site.register(Project, ProjectAdmin)
