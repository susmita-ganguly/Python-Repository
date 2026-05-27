#pip install azure-ai-translation-text==1.0.0b1
#This allows us to work with translation service
#The format ofalling this service is a bit different from what we have done before

from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem

endpoint=""
key=""
region="eastus" #for languae translation we need to provide the region

credential=TranslatorCredential(key,region)
client=TextTranslationClient(endpoint=endpoint,credential=credential)

source_language="en"
target_language=["it"]

input_txt="I like to learn new languages"
documents=[InputTextItem(text=input_txt)]

response=client.translate(content=documents,to=target_language,from_parameter=source_language)
print(f"Translated Text : {response[0].translations}")