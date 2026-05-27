#pip install azure.ai.textanalytics

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential)

documents=[
    "Me gusta aprender nuevos idiomas.",
    "Comment allez-vous ce matin ?"
]

response=client.detect_language(documents=documents)
print(response)