import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/audio', methods=['POST'])
def audio():
    with open('audio.wav', 'wb') as f:
        f.write(flask.request.data)
    return 'audio gravado'


if __name__ == "__main__":
    app.logger = flask.logging.create_logger(app)
    app.run(debug=True)
