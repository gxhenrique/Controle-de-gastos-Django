from django.shortcuts import render, redirect

# Create your views here.

from . forms import FormsModel
from . models import financaModel,UsuarioModel

def controle_financa(request):

    transacao = financaModel.objects.all()
    usuario = UsuarioModel.objects.get(id=1)
    # transacaos = financaModel.objects.get()

    total_entradas = sum(t.valor for t in transacao if t.tipo == 'entrada')
    total_saidas = sum(t.valor for t in transacao if t.tipo == 'saida')
    saldo = total_entradas - total_saidas

    soma = 0
    for teste in transacao:
        print(teste)
        if teste.tipo == 'entrada':
            soma += teste.valor

    print(soma)


    form = FormsModel()

    if request.method == 'POST':
        form = FormsModel(request.POST)
        

        # print(f'ISSO AQUI E UM TESTE: -------{request.POST['titulo']}---------- ')
        # print(f'ISSO AQUI E UM TESTE: -------{request.POST['valor']}---------- ')
        # print(f'ISSO AQUI E UM TESTE: -------{request.POST['tipo']}---------- ')
        # print("POST vindo:", request.POST)

        if form.is_valid():
            print("cleaned_data:", form.cleaned_data)
            financa = form.save(commit=False)
            financa.usuario = usuario
            #form.save()
            financa.save()
            return redirect('/')
        
    
    return render(request, 'pages/index.html', context={
        'form': form,
        'transacaos': transacao,
        'total_entrada': total_entradas,
        'total_saida': total_saidas,
        'saldo': saldo,
        'soma': soma,
        'usuario': usuario,
    })


def delete_financa(request, id):
    transacao = financaModel.objects.get(id=id)
    transacao.delete()
    return redirect('/')

def alterar_financa(request,id):

    transacao = financaModel.objects.get(id=id)
    
   
    if request.method == 'POST':
        titulo = request.POST['titulo']
        valor = request.POST['valor']
        tipo = request.POST['tipo']

        transacao.titulo = titulo
        transacao.valor = valor
        transacao.tipo = tipo

        transacao.save()
        return redirect('/')
        