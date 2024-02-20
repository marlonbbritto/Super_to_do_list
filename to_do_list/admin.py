from django.contrib import admin
from to_do_list.models import Tarefas

class ListTasks(admin.ModelAdmin):
    list_display = ("id", "user", "task", "deadline", "status","done","data_atualizacao_concluida")
    list_display_links = ("id","task")
    search_fields = ("task",)
    list_filter = ('user',)    
    list_per_page = 10
    
admin.site.register(Tarefas,ListTasks)