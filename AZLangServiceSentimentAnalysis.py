#pip install azure.ai.textanalytics

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
#Please replace with the endpoint from your Azure portal, for this resoirce
endpoint="https://language4000.cognitiveservices.azure.com/"
key=""

client=TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential)

documents=[
    "The restaurant had amazing food and the staff were incredibly findly"
    "The product arrived broken and customer service was unhelpful"
    "The report produced around 200 data points"
]

response=client.analyze_sentiment(documents=documents)

for result in response:
    print(f"Sentiment: {result.sentences[0].sentiment} - Sentence: {result.sentences[0].text}")