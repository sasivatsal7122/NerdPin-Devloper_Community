from django.contrib import admin
from git import Tag


from .models import Project, Review,Tag
# Register your models here.


admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)