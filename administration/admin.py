from django.contrib import admin

from administration.models import *

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Center)
admin.site.register(Project)
admin.site.register(ProjectTime)
admin.site.register(Workday)
admin.site.register(Pause)


