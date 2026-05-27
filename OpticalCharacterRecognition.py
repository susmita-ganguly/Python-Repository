#install the library using the following command in terminal <pip install azure-ai-vision-imageanalysis>

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json

endpoint=""
key=""

client=ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential)
with open("quote.png","rb") as image_file:
    image_details=image_file.read()

response=client.analyze(
    image_data=image_details,
    visual_features=[VisualFeatures.READ]

)
#typecasting the output as dictionary, taking it as a json string
for line in response.read.clocks[0].lines:
    print(f"{line.text}")