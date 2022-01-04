// FUNÇÃO PARA COLOCAR SOMBRA NA NAVBAR APÓS ROLAR A TELA:

$(window).scroll(function () {

    if ($(this).scrollTop() < 50) {
        $('.sticky-shadow').css({
            'box-shadow': 'none',
            '-moz-box-shadow': 'none',
            '-webkit-box-shadow': 'none'
        });
    }
    else {
        $('.sticky-shadow').css({
            'box-shadow': '0px 0px 5px rgba(0, 0, 0, 0.2)',
            '-moz-box-shadow': '0px 0px 5px rgba(0, 0, 0, 0.2)',
            '-webkit-box-shadow': '0px 0px 5px rgba(0, 0, 0, 0.2)'
        });
    }
});

// FUNÇÃO PARA REMOVER NAVBAR MOBILE SE CLICAR FORA DELA:

$(document).click(function (event) {
    if (!$(event.target).is('.navbar-collapse *')) {
        $('.navbar-collapse').collapse('hide');
    }
});

// TROCAR BOTÕES DE PESQUISA:

function replace(hide, show) {
    document.getElementById(hide).style.display = "none";
    document.getElementById(show).style.display = "block";
}

// LIBERAR POPOVER BARRA DE PESQUISA:

const popover = new bootstrap.Popover(document.querySelector('.ativar-popover-pesq'), {
    container: 'body',
    html: true,
    placement: 'bottom',
    sanitize: false,
    content() {
        return document.querySelector('#conteudo-popover').innerHTML;
    }
})


// FUNÇÃO PARA COLOCAR LIBERAR BOTÃO DE VOLTAR AO TOPO:

$(window).scroll(function () {

    if ($(this).scrollTop() < 500) {
        $('.btn-visivel').fadeOut();
    }
    else {
        $('.btn-visivel').fadeIn();
    }
});

// INICIAR TOAST COM TIMEOUT:

setTimeout(function () {
    let myAlert = document.getElementById('toast-promo-relampago'); 
    if (myAlert !== null) { // previne que em paginas que não existam a div do toast, um erro não ocorra
        let bsAlert = new bootstrap.Toast(myAlert);
        bsAlert.show();
    }
}, 7000);

