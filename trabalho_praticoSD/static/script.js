function pesquisarVideos(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário

    var termoPesquisa = document.getElementById("termoPesquisa").value;

    $.ajax({
        url: '/api/videos', // Rota para a API no Flask
        type: 'POST',
        data: { termo: termoPesquisa },
        success: function(response) {
            var resultadosDiv = document.getElementById("resultados");
            resultadosDiv.innerHTML = response;
        }
    });
}
