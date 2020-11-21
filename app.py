import flask
import numpy as np
import librosa
from joblib import load
app = flask.Flask(__name__)

model = load("modelo.joblib")
def predicao(p_nomeArquivo):

    X, sample_rate = librosa.load(os.path.join(p_nomeArquivo), res_type='kaiser_fast')

    stft=np.abs(librosa.stft(X))
    atributos=np.array([])

    mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
    atributos=np.hstack((atributos, mfccs))

    chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    atributos=np.hstack((atributos, chroma))

    mel=np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    atributos=np.hstack((atributos, mel))
    x = []
    x.append(atributos)
    stri = model.predict(x)[0]
    return stri

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/audio', methods=['POST'])
def audio():
    with open('audio.wav', 'wb') as f:
        f.write(flask.request.data)
    previsao = str(predicao('audio.wav'))
    return previsao


if __name__ == "__main__":
    app.logger = flask.logging.create_logger(app)
    app.run(debug=True)
