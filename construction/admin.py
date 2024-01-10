from django.contrib import admin
from .models import Project, ProjectImage, ProjectPDF

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage

class ProjectPDFInline(admin.TabularInline):
    model = ProjectPDF

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ProjectPDFInline]

admin.site.register(Project, ProjectAdmin)
