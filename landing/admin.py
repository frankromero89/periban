from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

from landing.models import Profile as Profile, Form_type, Question_form, answer_form, image_evidence


# Register your models here.
@admin.register(Form_type)
class FormTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'form_name')


# class QuestionInline(SortableInlineAdminMixin, admin.StackedInline):
#     model = Question_form
#     can_delete = False
#     verbose_name_plural = 'question'
@admin.register(Question_form)
class QuestionFormsAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('question_description', 'form_type', 'is_active')

@admin.register(image_evidence)
class ImageEvidenceAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('form_id', 'image_evidence',)

@admin.register(answer_form)
class AnswerFormsAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'question_id', 'answer')


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