from django.urls import path

from . import views

urlpatterns = [
    path('', views.controle_financa, name='controle_financa'),
    path('delete/<int:id>', views.delete_financa, name='delete_financa'),
    path('alterar/<int:id>', views.alterar_financa, name='alterar_financa')
]
