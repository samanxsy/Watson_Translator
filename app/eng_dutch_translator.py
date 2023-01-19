import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

API_KEY =  os.environ.get("watson_API_KEY")
URL = "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/c36cf875-e213-453e-bfab-31d31d3b9fe4"

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(URL)

def english_to_dutch(text1):
    """
    This function translates the text from English to Dutch and vice versa
    """
    
    translation = language_translator.translate(text=text1, model_id='en-nl').get_result()

    return translation.get('translations')[0].get('translation')
    

