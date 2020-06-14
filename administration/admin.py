from django.contrib import admin

from administration.models import *

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Center)
admin.site.register(Project)

class ProjectTimeAdmin(admin.ModelAdmin):
    list_display = ['project', 'user']
admin.site.register(ProjectTime, ProjectTimeAdmin)
admin.site.register(Workday)
admin.site.register(Pause)


