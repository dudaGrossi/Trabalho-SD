from flask import Flask,render_template
from youtubeApi import getComments

app=Flask(__name__,template_folder='template')

#criar a 1° página do site
#route -> comentariosyoutube.com
#função -> o que vc quer exibir naquela página
@app.route("/")
def home():
    videoId = 'HXZZEJap3Lg'
    comments = getComments(videoId)
    return render_template("home.html", comments=comments)

@app.route("/about/")
def about():
    return render_template('about.html')

#colocar o site no ar
if __name__=="__main__":
    app.run(debug=True)