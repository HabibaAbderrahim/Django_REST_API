from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Course

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    pass
#admin.site.register
