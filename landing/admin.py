from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from adminsortable2.admin import SortableAdminMixin
from import_export.admin import ExportActionMixin    

from landing.models import Profile as Profile, Form_type, Question_form, answer_form, image_evidence, promedy_form


# Register your models here.
@admin.register(Form_type)
class FormTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'form_name')

@admin.register(Question_form)
class QuestionFormsAdmin(ExportActionMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ('question_description', 'form_type', 'is_active')

@admin.register(image_evidence)
class ImageEvidenceAdmin(ExportActionMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ('form_id', 'image_evidence',)

@admin.register(answer_form)
class AnswerFormsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('form_id', 'question_id', 'answer')

@admin.register(promedy_form)
class AnswerFormsAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('form_id', 'promedy_form')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'role')
    list_editable = ('role',)


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)