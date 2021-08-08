from django.contrib import admin

from reviews.models import Publisher, Contributor, Book, BookContributor, Review


def initialed_name(contributor):
    """Name of contributor with only first names' initials. E.g. Pax, RW"""
    fn_initials = ''.join(name[0] for name in contributor.first_names.split(' '))
    return f"{contributor.last_names}, {fn_initials}"


class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialed_name,)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn13')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
