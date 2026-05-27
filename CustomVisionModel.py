#install the following in terminal: pip install azure-cognitiveservices-vision-customvision

from msrest.authentication import ApiKeyCrdentials
from azure.cognitiveservices.visiob.customvision.prediction import CustomVisionPredictionClient

endpoint=""
key=""

credentials = ApiKeyCredentials(in_headers={"Prediction-key":key})
prediction_client=CustomVisionPredictionClient(endpoint=endpoint, credentials=credentials)

image_data=open("img.jpeg", mode="rb").read()
#Project id will be in the customvision.ai site under settings
projectid=""
#model name we can see in the model published window itself while publishing
model_name=""

response=prediction_client.classify_image(projectid,model_name,image_data)

for prediction in response.predictions:
    print(prediction)

#we get a json response with probability of prediction in decimal, so 0.96... is 96%, 
# tag_name as the classification, the bounding box and so on...