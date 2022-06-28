from django.contrib import admin
from data.models import *

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "start_date")

class ExperienceSARAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ExperienceSAR, ExperienceSARAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Contact, ContactAdmin)
