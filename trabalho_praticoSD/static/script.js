function pesquisarVideos(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário

    var termoPesquisa = document.getElementById("termoPesquisa").value;

    $.ajax({
        url: '/api/videos', // Rota para a API no Flask
        type: 'POST',
        data: { termo: termoPesquisa },
        success: function(response) {
            var resultadosDiv = document.getElementById("resultados");
            resultadosDiv.innerHTML = ""; // Limpa o conteúdo anterior
        
            // Adiciona os resultados da pesquisa ao HTML
            for (var i = 0; i < response.resultados.length; i++) {
                var video = response.resultados[i];
                resultadosDiv.innerHTML += "<p>" + video.title + " - ID: " + video.video_id + "</p>";
            }
        }        
    });
}
