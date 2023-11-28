# YoutubeComments

O projeto **YoutubeComments** foi desenvolvido como parte da disciplina de Sistemas Distribuídos do curso de Ciência da Computação da Universidade Federal de Lavras (UFLA). O objetivo do projeto é realizar Web Scraping em vídeos do Youtube utilizando Flask. Isso permite obter informações sobre 5 vídeos relacionados a um tema específico, incluindo 5 comentários para auxiliar na decisão de assistir ou não ao vídeo. O projeto é desenvolvido em Python, com a interface do usuário em HTML, e foi utilizado o VSCode como plataforma de desenvolvimento.

## Índices
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplos de Uso](#exemplos-de-uso)
- [Configuração](#configuração)
- [Contribuição](#contribuição)
- [Contato](#contato)

## Instalação

Certifique-se de ter o Python e o pip instalados. Execute os seguintes comandos para instalar as dependências necessárias:

```bash
pip install flask
pip install google-auth-oauthlib
pip install google-auth
pip install google-api-python-client
pip install matplotlib
pip install wordcloud
pip install nltk
```

## Como Usar

Para usar o projeto, siga estas etapas:

1. Clone o repositório para o seu ambiente local:
```bash
git clone https://github.com/seu-username/YoutubeComments.git
```
2. Abra o terminal na pasta do projeto.
3. Execute o comando:
```bash
python app.py
```
4. Abra o navegador e vá para http://127.0.0.1:5000/.
5. Insira o termo de pesquisa na caixa de texto e clique em "Pesquisar".

## Exemplos de Uso
- Após a pesquisa, você receberá uma lista de vídeos do Youtube relacionados ao termo pesquisado.
- Cada vídeo inclui um link para o vídeo no Youtube, os cinco primeiros comentários e uma nuvem de palavras com as palavras mais comentadas.

## Configuração
Não é necessário configurar nada além das instruções de instalação. Certifique-se de ter uma conexão com a internet para acessar o Youtube.

## Contribuição
Se quiser contribuir para o projeto, siga os passos abaixo:
1. Faça um fork do repositório no GitHub.
2. Clone o fork para o seu ambiente local:
```bash
git clone https://github.com/seu-username/YoutubeComments.git
```
3. Crie uma branch para suas alterações:
```bash
git checkout -b minha-contribuicao
```
4. Faça as alterações desejadas.
5. Commit e push para o seu fork:
```bash
git add .
git commit -m "Minha contribuição"
git push origin minha-contribuicao
```
6. Abra um pull request no repositório original.

## Contato
Para sugestões ou mais informações, entre em contato:
- @dudaGrossi - maria.grossi1@estudante.ufla.br
- @matheusdinizdev - matheus.diniz@estudante.ufla.br
- @raissaro - raissa.oliveira@estudante.ufla.br