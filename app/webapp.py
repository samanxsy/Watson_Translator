import eng_dutch_translator
from flask import Flask, request

app = Flask('Watson Translator', static_folder="./app/static")

@app.route('/')
def home():
    
    """
    This is the home page, our layout.html file
    """
    
    page = ""
    f = open("app/templates/layout.html", "r")
    page = f.read()
    f.close()

    return page
    
@app.route('/translate')
def toTranslate():
    
    """
    This function will get the text and then reutrn the translation
    """

    page = ""
    f = open("app/templates/layout.html", "r")
    page = f.read()
    f.close()
    
    textToTranslate = request.args.get('text_to_translate')
    translated_text = eng_dutch_translator.english_to_dutch(textToTranslate)

    page = page.replace("|||", translated_text)
    
    return page


if __name__ == '__main__':
    app.run(debug=True)