from django.contrib import admin

from .models import Question, Choice

# Register your models here.
# admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] # filter by date on the right side
    search_fields = ['question_text'] #uses a LIKE query behind the scenes, so try to limit the number of search fields

    # first element of each tuple in fieldsets is the title of the fieldset.

admin.site.register(Question, QuestionAdmin)

# create an admin model class, then pass it as the second argument to admin.site.register(),
# any time you need to change the admin options for a model
# good for re-ordering fields on particularly complex forms, for good readability and usability
