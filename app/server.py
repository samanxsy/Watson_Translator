from . import watson
from flask import Flask, request
from flask_talisman import Talisman
from app.common.errorhandlers import EmptyInput

app = Flask('Watson Translator', static_folder="./app/static")

# Disable the following lines for TESTING purposes, but KEEP them ENABLED for production
csp = {
    'default-src': '\'self\'',
    'img-src': '*'
}
talisman = Talisman(
    app,
    content_security_policy=csp,
    force_https=True,
    strict_transport_security=True,
    session_cookie_secure=True,
    session_cookie_http_only=True,
    frame_options='DENY'
)


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

    invalid_pair_error_msg = "Sorry!\nTranslation is not available for this pair!"
    empty_input_error_msg = "Please enter some text to translate!"

    try:
        if not textToTranslate.strip():
            raise EmptyInput(empty_input_error_msg)

        translated_text = watson.translate(textToTranslate, model_id)
        page = page.replace("Translation will appear here...", translated_text)
        return translated_text

    except EmptyInput:
        page = page.replace("Translation will appear here...", empty_input_error_msg)
        return empty_input_error_msg

    except Exception:
        page = page.replace("Translation will appear here...", invalid_pair_error_msg)
        return invalid_pair_error_msg
