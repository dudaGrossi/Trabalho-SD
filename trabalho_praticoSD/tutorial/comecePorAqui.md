# Olá! Esse é o tutorial da atividade proposta em sala.

O objetivo desse tutorial é te fornecer o passo a passo do que precisa ser feito para que você possa testar a parte básica do nosso programa. Por meio desse tutorial, você aprenderá a gerar sua própria chave API do Youtube e utilizá-la para recuperar comentários de vídeos de um assunto que você definir. Iremos utilizar o Replit para esse tutorial para fins de facilitar em questões de instalação de bibliotecas.

## Gerando sua Youtube API-Key

Para gerar sua chave API do Youtube, siga os passos especificados no README do projeto:
1. Primeiro, é necessário ter uma Conta do Google para acessar o Console de APIs, solicitar uma chave de API e registrar seu aplicativo.

2. Inicie criando um projeto no [Google Developers Console] (https://console.developers.google.com/?hl=pt-br) para obter as credenciais de autorização. Isso permitirá que seu aplicativo envie solicitações de API.

3. Após criar o projeto, verifique se a API do YouTube Data está habilitada para uso pelo seu aplicativo:
  a. Acesse o Console de APIs e selecione o projeto recém-criado.
  b. Vá para a página de APIs ativadas. Verifique na lista de APIs se a API do YouTube Data v3 está habilitada e com status ATIVADO para garantir seu 
  funcionamento corretamente pelo aplicativo.

Para mais informações consulte o site: [Visão geral da API YouTube Data] (https://developers.google.com/youtube/v3/getting-started?hl=pt-br)

## Utilizando sua chave no projeto

Na pasta 'tutorial', onde está esse arquivo, está o arquivo texto api-youtube.txt. 
1. Encontre esse arquivo na pasta.
2. Abra no Replit um projeto em Python (https://replit.com/).
3. Copie no seu projeto Replit o conteúdo do arquivo texto api-youtube.txt.
4. Modifique no replit a chave API do Youtube: 
```bash
api_key = "YOUR_API_KEY"
```
5. Escolha o tema que deseja pesquisar em:
```bash
resultados = search_videos('tema', max_results=5)
```