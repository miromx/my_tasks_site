from django.contrib import admin
from .models import Must, May, Want, Rubric

# Register your models here.
# class TasksAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content', 'price', 'published', 'rubric')
#     list_display_links = ('title', 'content')
#     search_fields = ('title', 'content',)


admin.site.register(Must)
admin.site.register(May)
admin.site.register(Want)
admin.site.register(Rubric)
