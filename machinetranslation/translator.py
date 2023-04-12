import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

## API
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
translator.set_service_url(url)

def english_to_french(english): ## English to French
    if not english:
        return ''
    translation = translator.translate(english, source='en', target='fr').get_result()
    french = translation['translations'][0]['translation']
    return french

def french_to_english(french): ## French to English
    if not french:
        return ''
    translation = translator.translate(french, source='fr', target='en').get_result()
    english = translation['translations'][0]['translation']
    return english
