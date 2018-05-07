# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from models import *


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'text', )


class QuestionTranslationOptions(TranslationOptions):
    fields = ('title_short', 'title_long', 'text')


translator.register(Service, ServiceTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
translator.register(Question, QuestionTranslationOptions)
