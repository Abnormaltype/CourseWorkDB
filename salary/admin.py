from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Project, Bonus, PersonBonusProject, Wage, Main, Person, ReportCard

admin.site.register(Project)
admin.site.register(Bonus)
admin.site.register(PersonBonusProject)
admin.site.register(Main)
admin.site.register(Wage)
admin.site.register(ReportCard)


@admin.register(Person)
class PersonAdmin(UserAdmin):
    pass
