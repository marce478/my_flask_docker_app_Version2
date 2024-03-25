from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Updated Flask Docker App Version 2! Visit /translate to translate words.'

def mock_translate(text, target_lang="Spanish"):
    return f"{text} [Translated to {target_lang}]"

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        english_text = request.form.get('english_text', '')
        translated_text = mock_translate(english_text)
    else:
        translated_text = ""
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Translate to Spanish</title></head>
        <body>
            <h2>Translate English to Spanish</h2>
            <form method="post">
                <textarea name="english_text" rows="4" cols="50" placeholder="Enter English text here"></textarea><br>
                <input type="submit" value="Translate">
            </form>
            <p>Translation: {{ translated_text }}</p>
        </body>
        </html>
    ''', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
