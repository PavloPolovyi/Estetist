from django.contrib import admin
from .models import Post, Comment, Category
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


class PostAdminForm(forms.ModelForm):
    body_ru = forms.CharField(label=_('Текст поста_ru'),
                              widget=CKEditorUploadingWidget())
    body_uk = forms.CharField(label=_('Текст поста_uk'),
                              widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    filter_horizontal = ('category',)
    list_filter = ('status', 'created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title', )}
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    inlines = [PostInline]
    save_on_top = True
    form = PostAdminForm


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    readonly_fields = ('name', 'email')
    list_editable = ('active', )


admin.site.site_title = 'Estetist'
admin.site.site_header = 'Estetist'