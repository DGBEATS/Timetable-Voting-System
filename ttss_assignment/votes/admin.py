from django.contrib import admin

from .models import Question, Option

# change the site header, title
# admin.site.site_header = "Crescent Admin"
# admin.site.site_title = "Crescent Admin Area"
# admin.site.index_title = "Welcome to the Crescent Admin Page"


class OptionInLine(admin.TabularInline):
    model = Option
    extra = 5

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None, 
            {
                'fields': ['question_text']
            }
        ),
                (
                    'Date Information', 
                    {
                        'fields': ['publish_date'],
                        'classes': ['collapse']
                    }
                ),
        ]
    inlines = [OptionInLine]


admin.site.register(Question, QuestionAdmin)
