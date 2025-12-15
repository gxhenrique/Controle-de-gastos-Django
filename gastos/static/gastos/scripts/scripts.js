let botao_alterar = document.querySelectorAll('.botao_alterar')
let botao_salvar = document.querySelectorAll('.botao_salvar')
let input_titulo = document.querySelectorAll('.input_titulo')
let input_valor = document.querySelectorAll('.input_valor')
let select_tipo = document.querySelectorAll('.select_tipo')

botao_alterar.forEach((botao, index) => {
    botao.addEventListener('click', () => {
        botao_alterar[index].style.display = 'none'
        

        botao_salvar[index].style.display = 'inline-block'

        
        input_titulo[index].removeAttribute('disabled')
        input_valor[index].removeAttribute('disabled')
        select_tipo[index].removeAttribute('disabled')
    })
})