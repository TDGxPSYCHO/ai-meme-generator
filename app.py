from flask import Flask, render_template, request
from meme_generator import create_meme

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    meme_path = None
    if request.method == 'POST':
        topic = request.form['topic']
        meme_path = create_meme(topic)
    return render_template('index.html', meme_path=meme_path)

if __name__ == '__main__':
    app.run(debug=True)