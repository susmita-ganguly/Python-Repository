# pip install azure-cognitiveservices-speech
import azure.cognitiveservices.speech as speechsdk

endpoint=""
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)

output_file="transcribed.txt"
audio_filename="speech01.wav"
config.speech_recognition_language="en-US"

audio_input=speechsdk.AudioConfig(filename=audio_filename)
txt_generator=speechsdk.SpeechRecognizer(speech_config=config,audio_config=audio_input)

result=txt_generator.recognize_once_async().get()
#write in output file only if the speech is recognized
#so bascially here the service is trying to recognize the speech
if result.reason==speechsdk.ResultReason.RecognizedSpeech:
    print("Successfully generated text")
    with open(output_file,"w",encoding="utf-8") as file:
        file.write(result.text)

else:
    print("Generating text failed")
# Issue with this program is, it will consider the speech till a 
# break or a pause, we will get the output text upto the first break
# In order to get the entire speech converted, we will need to run a loop
# which will read till the end. This loop's syntax is available in 
# MS documentation 