from .models import Post, Category

from modeltranslation.translator import register, TranslationOptions


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'body')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug' )
