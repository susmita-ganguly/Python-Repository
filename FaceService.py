<pip install azure-ai-vision-face>
#install the library
#This is a python program to interact with the face service of Azure
from azure.core.credentails import AzureKeyCredential
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
endpoint="<your endpoint from the resource created>"
key=""

client=FaceClient(endpoint=endpoint,credential=AzureKeyCredential(key))
features_to_client=[
    FaceAttributeTypeDetection01.HEAD_POSE,
    FaceAttributeTypeDetection01.OCCLUSION,
    FaceAttributeTypeDetection01.ACCESSORIES
]

with open("face.jpg", mode="rb") as image_data:
    response=client.detect(
        image_content=image_data.read(),
        detection_model=FaceDetectionModel.DETECTION01,
        recognition_model=FaceRecognitionModel.RECOGNITION01,
        return_face_id=False,
        return_face_attributes=features_to_client
    )

    print(json.dumps(response[0].as_dict(),indent=4))
