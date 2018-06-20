from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from models import *


class ServiceAdmin(TabbedTranslationAdmin):
    pass


class ProjectAdmin(TabbedTranslationAdmin):
    pass


class QuestionAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Question, QuestionAdmin)
