from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from youtubeApi import getComments, search_videos

app = Flask(__name__, template_folder='template', static_url_path='')

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/api/videos', methods=['POST'])
def buscar_videos():
    termo_pesquisa = request.form['search']
    videos = search_videos(termo_pesquisa)[:5]
    comentarios_por_video = []

    for video in videos:
        video_id = video['video_id']
        comentarios = getComments(video_id)[:5]
        comentarios_por_video.append({'video': video, 'comentarios': comentarios})

    return render_template("home.html", comentarios_por_video=comentarios_por_video)

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route('/imagens/<path:filename>')
def download_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'imagens'), filename)

if __name__=="__main__":
    app.run(debug=True)
