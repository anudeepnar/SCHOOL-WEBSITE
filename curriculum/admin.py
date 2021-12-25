from django.contrib import admin
from django.contrib.admin.decorators import register
from curriculum.models import Standard, Subject, Lesson
# Register your models here.

class AdminStandard(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class AdminSubject(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('subject_id',)}

class AdminLesson(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('lesson_id',)}

admin.site.register(Standard, AdminStandard)
admin.site.register(Subject, AdminSubject)
admin.site.register(Lesson, AdminLesson)