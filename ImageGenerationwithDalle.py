
from openai import AzureOpenAI
import requests
#endpoint= os.getenv("ENDPOINT_URL", "https://amrit-mnmty46i-eastus2.openai.azure.com/")


client = AzureOpenAI(
    azure_endpoint="",
    api_key="",
    api_version="2025-01-01-preview",
)

response=client.images.generate(
    model="dall-e-3",
    prompt="A futuristic cat dwelling in the background, very detailed, digital art",
    n=1,
    size="1024x1024"
    quality="standard"
)
image_url=response.data[0].url
image_data=requests.get(image_url).context 
with open("img2.png","wb") as handler:handler.write(image_data)

print("finished generating the image")
