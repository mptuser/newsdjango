from django.contrib import admin
from .models import Notes, Comments, Tags

# admin.site.register(Notes)
admin.site.register(Comments)
admin.site.register(Tags)


class CommentsInLine(admin.TabularInline):
    model = Comments
    extra = 0


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    fields = ('title', ('author'), 'text', 'fk_tag')
    inlines = [CommentsInLine,]