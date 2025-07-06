from flask import Flask, request, send_file, render_template
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    text = data.get('text', '')
    tts = gTTS(text=text, lang='bn')
    audio_io = io.BytesIO()
    tts.write_to_fp(audio_io)
    audio_io.seek(0)
    return send_file(audio_io, mimetype='audio/mpeg', as_attachment=True, download_name='bengali_audio.mp3')

if __name__ == '__main__':
    app.run(debug=True)
