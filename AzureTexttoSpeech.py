# pip install azure-cognitiveservices-speech
import azure.cognitiveservices.speech as speechsdk

endpoint=""
key=""

config=speechsdk.SpeechConfig(subscription=key,endpoint=endpoint)
config.speech_synthesis_voice_name="en-US-SteffanMultilingualNeutral"

input_txt="Machine learning is a branch of artificial intelligence (AI) that helps in" \
"building systems that can learn from data and improve over time without being" \
"blah blah"

output_file="speech01.wav"
audio_output=speechsdk.audio.AudioConfig(filename=output_file)

speech_generator=speechsdk.SpeechSynthesizer(speech_config=config,audio_config=audio_output)
result=speech_generator.speak_text_async(input_txt).get()
if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Successfully generated speech")

else:
    print("Generating speech failed")
    