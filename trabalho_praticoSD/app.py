from flask import Flask, render_template, request, send_from_directory
import os
from youtubeApi import getComments, search_videos, save_to_csv
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import base64
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

app = Flask(__name__, template_folder='template', static_url_path='')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/api/videos', methods=['POST'])
def buscar_videos():
    termo_pesquisa = request.form['search']
    videos = search_videos(termo_pesquisa)[:5]
    comentarios_por_video = []
    wordclouds_por_video = []

    for video in videos:
        video_id = video['video_id']
        comentarios = getComments(video_id)[:5]

        # Adicione a URL do vídeo aos resultados
        video['url'] = f"https://www.youtube.com/watch?v={video_id}"

        # WordCloud para os cinco primeiros comentários de cada vídeo
        wordcloud = WordCloud(
            background_color='black',
            width=400,
            height=200,
            stopwords=set(stopwords.words('portuguese'))
        ).generate(' '.join(comentario['comment'] for comentario in comentarios))

        # Adiciona os dados nas listas
        comentarios_por_video.append({'video': video, 'comentarios': comentarios})
        wordclouds_por_video.append({'video': video, 'wordcloud': wordcloud})

        #Salva os dados no csv
        save_to_csv(video, comentarios)

    # Gera as imagens das nuvens de palavras e salva temporariamente
    imagens_por_video = []
    for i, wordcloud_data in enumerate(wordclouds_por_video):
        wordcloud = wordcloud_data['wordcloud']
        img_path = f'temp_wordcloud_{i}.png'
        wordcloud.to_file(img_path)
        imagens_por_video.append(img_path)

    # Converte as imagens para base64 para envio para a página web
    imagens_base64 = []
    for img_path in imagens_por_video:
        with open(img_path, 'rb') as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode('utf-8')
            imagens_base64.append(img_base64)

    # Remove as imagens temporárias
    for img_path in imagens_por_video:
        os.remove(img_path)

    # Retorna HTML se a solicitação não for AJAX, senão retorna JSON
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        return render_template("home.html", comentarios_por_video=comentarios_por_video, wordclouds_por_video=wordclouds_por_video, imagens_base64=imagens_base64)

    return {
        'comentarios_por_video': comentarios_por_video,
        'imagens_base64': imagens_base64
    }

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route('/imagens/<path:filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'imagens'), filename)

if __name__=="__main__":
    app.run(debug=True)
