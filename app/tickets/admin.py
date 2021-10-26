from django.contrib import admin
from .models import Quera, Ticket


class QueraAdmin(admin.ModelAdmin):
    fields = ['name']
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_author_name']
    fields = ['title', 'author', 'content'] #author é referencia
    readonly_fields = ['created_on']

    def get_form(self, request, obj=None, **kwargs):
        form = super(TicketAdmin, self).get_form(request, obj, **kwargs)
        authorField = form.base_fields["author"]
        authorField.widget.can_add_related = True
        authorField.widget.can_change_related = False
        authorField.widget.can_delete_related = False
        authorField.empty_label = 'No value'

        return form

    # def get_queryset(self, request):
    #     return super(TicketAdmin,self).get_queryset(request).select_related('book')

    # sem performance
    @admin.display(
        ordering='author__name',
        description='Nome do author',
    )
    def get_author_name(self, obj):
        return obj.author.name or "Sem Author"
# Register your models here.
admin.site.register(Quera, QueraAdmin)
admin.site.register(Ticket, TicketAdmin)


