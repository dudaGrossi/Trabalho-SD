from flask import Flask, render_template, request, jsonify
from youtubeApi import getComments, search_videos

app=Flask(__name__,template_folder='template')

#criar a 1° página do site
#route -> comentariosyoutube.com
#função -> o que vc quer exibir naquela página
@app.route("/")
def home():
    videoId = 'HXZZEJap3Lg'
    comments = getComments(videoId)
    return render_template("home.html", comments=comments)

@app.route('/api/videos', methods=['POST'])
def buscar_videos():
    termo_pesquisa = request.form['termo']
    resultados = search_videos(termo_pesquisa)
    return jsonify(render_template('home.html', videos=resultados))


@app.route("/about/")
def about():
    return render_template('about.html')

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True) 
