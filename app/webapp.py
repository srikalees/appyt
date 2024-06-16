from flask import Flask, request, render_template,send_file
from flask_bootstrap import Bootstrap
from main import download_video

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
     return render_template('index.html')

@app.route("/main", methods=['POST'])
def download():
    videos_url =request.form['firstvideo']
    download_video(videos_url)

    return render_template('index.html')
@app.route('/download')
def download_file():
    filename = 'path_to_your_file/example.txt'
    # Perform logging or database updates here
    (f"File download successful: {filename}")
    return send_file(filename, as_attachment=True)






if __name__=='__main__':
    app.run(port=5000,debug=True)