from django.contrib import admin
from .models import Author, Book, Genre, Language, Status, BookInstanse


# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstanse)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


admin.site.register(Author, AuthorAdmin)


class BookInstanseInline(admin.TabularInline):
    model = BookInstanse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    list_filter = ('genre', 'author')
    inlines = [BookInstanseInline]


@admin.register(BookInstanse)
class BookInstanseAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземляр книги', {'fields': ('book', 'imprint', 'inv_nom')}),
        ('Статус и окончание его действия', {'fields': ('status', 'due_back', 'borrower')})
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)

# Register your models here.
