from django.db import models

# Create your models here.

TIPO_CHOICE = (
    ('entrada', 'Entrada'),
    ('saida', 'Saída'),
)



class UsuarioModel(models.Model):
    
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=12)

    def __str__(self):
        return self.email


class financaModel(models.Model):
    usuario = models.ForeignKey(UsuarioModel, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=20,decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICE)
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
