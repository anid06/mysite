from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('question_text', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text','question', 'votes')
    list_filter = ('choice_text','question', 'votes')
    ordering = ['-question', '-votes']
    autocomplete_fields = ['question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

