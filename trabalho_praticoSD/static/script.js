function pesquisarVideos(event) {
    event.preventDefault(); // Evita o comportamento padrão do formulário

    var termoPesquisa = document.getElementById("termoPesquisa").value;

    $.ajax({
        url: '/api/videos', // Rota para a API no Flask
        type: 'POST',
        data: { search: termoPesquisa },  // Corrija o nome do parâmetro para 'search'
        dataType: 'json',  // Indica que a resposta esperada é JSON
        success: function(response) {
            var resultadosDiv = document.getElementById("resultados");
            resultadosDiv.innerHTML = ""; // Limpa o conteúdo anterior

            // Adiciona os resultados da pesquisa ao HTML
            for (var i = 0; i < response.comentarios_por_video.length; i++) {
                var videoData = response.comentarios_por_video[i];
                var wordcloudData = response.imagens_base64[i];

                resultadosDiv.innerHTML += "<h2><a href='" + videoData.video.url + "' target='_blank'>" + videoData.video.title + "</a></h2>";
                
                // Adiciona os comentários
                for (var j = 0; j < videoData.comentarios.length; j++) {
                    var comentario = videoData.comentarios[j];
                    resultadosDiv.innerHTML += "<p>" + comentario.comment + " - " + comentario.author + "</p>";
                }

                // Adiciona a Word Cloud
                resultadosDiv.innerHTML += "<h3>Word Cloud</h3>";
                resultadosDiv.innerHTML += "<img src='data:image/png;base64," + wordcloudData + "' alt='Word Cloud'>";
            }
        }        
    });
}
