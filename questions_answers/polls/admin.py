from django.contrib import admin


# These are used to change the headers that shows in the django admin. 
# In the case where you are building an app for a client who might be using the django admin, 
# It is best to change to admin headers to suite the type of project. 
# In our case, this is a compulsory thing to do but it is good to learn

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"


# admin.site.register(Question)
# admin.site.register(Choices)

# We use this so that we want to see the choice associated to each question. 
# So instead of the normal way, we use the following
from .models import Question, Choice

class ChoicesInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),]
    inlines = [ChoicesInline]

admin.site.register(Question, QuestionAdmin)
