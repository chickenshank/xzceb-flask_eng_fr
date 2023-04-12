from flask import Flask, render_template, request
from machinetranslation import translator
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/english_to_french')
def english_to_french():
    english = request.args.get('text')
    french = translator.english_to_french(english)
    return french

@app.route('/french_to_english')
def french_to_english():
    french = request.args.get('text')
    english = translator.french_to_english(french)
    return english
