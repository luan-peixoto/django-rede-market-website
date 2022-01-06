function mostrarCard(id) {
    var elementos = document.querySelectorAll('.todos,.familia,.gourmet,.pratico')
    for (let elemento of elementos) {
        if (elemento.classList.contains(id)) {
            elemento.style.setProperty("display", "block", "important");
            console.log(elemento)
        }
        else {
            console.log(elemento)
            elemento.style.setProperty("display", "none", "important");
        }
    }
}