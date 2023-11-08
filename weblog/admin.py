from django.contrib import admin
from .models import Weblog

class WeblogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    def text(self,obj):
        return obj.body[:20]
    text.short_body = 'body'
    
admin.site.register(Weblog,WeblogAdmin)