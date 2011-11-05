from SocialScrum.ScrumBoard.models import Story
from SocialScrum.ScrumBoard.models import Task
from django.contrib import admin

# register Story as editable for the admin interface
# to embedd a task in the Story View
# admin.StackedInline:
#    every Task has an own box
# admin.TabularInline:
#    all Tasks are in one box in tabular form
class TaskInline(admin.StackedInline):
    model = Task
    extra = 1


class StoryAdmin(admin.ModelAdmin):
    # for reordering the fields in the admin interface
    fieldsets = [
              ('General',   {
                             'fields' : ['title', 'description'],
                            }),
              ('Duration',  {
                             'fields' : ['start', 'end'], 
                             # add collapse to collapse fieldset Duration
                             'classes': ['collapse']
                             }),
              ('Rating',    {
                             'fields' : ['rating']
                             })
              ]
    #embedds the Task in this Story View
    inlines = [TaskInline]
    list_filter = ['start']
    search_fields = ['title']
    date_hierachy = ['start']
    
    
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'start', 'in_progress')
    list_filter = ['story', 'start']
    search_fields = ['title', 'story']
    
# register the Admin Sites
admin.site.register(Story, StoryAdmin)
admin.site.register(Task, TaskAdmin)
