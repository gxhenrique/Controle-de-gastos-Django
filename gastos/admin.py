from django.contrib import admin

# Register your models here.
from . models import financaModel, UsuarioModel


@admin.register(UsuarioModel)
class UsuarioAdmin(admin.ModelAdmin):
    display = {'nome', 'email','senha'}


@admin.register(financaModel)
class FinancaAdmin(admin.ModelAdmin):
    display = {'titulo', 'valor','tipo'}

