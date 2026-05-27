#pip install azure.ai.textanalytics

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
#Please replace with the endpoint from your Azure portal, for this resoirce
endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential)

documents=[
    "Machine Learning and Artifical Intelligence are transforming industries "
    "such as healthcare, finance and education by automating tasks and providing insights"
]

response=client.extract_key_phrases(documents=documents)[0]
print(key_phrase)