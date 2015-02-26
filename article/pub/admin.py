from django.contrib import admin
from pub.models import Poll, Choice, Article, Author, Language, Journal
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]


class LanguageInline(admin.TabularInline):
    model = Language
    extra = 2


class JournalInline(admin.TabularInline):
    model = Journal


#class ArticleAdmin(admin.ModelAdmin):

admin.site.register(Poll, PollAdmin)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Journal)
admin.site.register(Article)
