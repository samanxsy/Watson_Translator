from . import watson
from flask import Flask, request

app = Flask('Watson Translator', static_folder="./app/static")


@app.route('/')
def home():
    """
    This is the home page, our layout.html file
    """

    page = ""
    F = open("app/templates/layout.html", "r")
    page = F.read()
    F.close()

    return page


@app.route('/translate', methods=['GET'])
def toTranslate():    
    """
    This function will get the text and then reutrn the translation
    """

    page = ""
    F = open("app/templates/layout.html", "r")
    page = F.read()
    F.close()

    textToTranslate = request.args.get('text_to_translate')
    text_language = request.args.get('text_model')
    translation_language = request.args.get('translate_model')
    model_id = f"{text_language}-{translation_language}"

    error_msg = "Sorry!\nTranslation is not available for this pair!"

    try:
        translated_text = watson.translate(textToTranslate, model_id)
        page = page.replace("Type something . . . ", textToTranslate)
        page = page.replace("Translation", translated_text)

    except:
        page = page.replace("Translation", error_msg)

    return page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
