from django.contrib import admin

from estudo.base.models import Aula, Categoria


@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
