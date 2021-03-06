from django.contrib import admin

from .models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Display individual fields
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Add a filter option for pub_date
    list_filter = ['pub_date']

    # Add some search fields
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Choice)