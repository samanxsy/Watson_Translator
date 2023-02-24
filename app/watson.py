import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY = secrets.watson_API_KEY
URL = "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/c36cf875-e213-453e-bfab-31d31d3b9fe4"

#  #  #  instance
authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(URL)


def translate(user_text, model):
    """
    This function translates the given text to the target language
    """

    translation = language_translator.translate(text=user_text, model_id=f'{model}').get_result()

    return translation.get('translations')[0].get('translation')
