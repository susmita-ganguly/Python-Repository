import openai from OpenAI
import base64


api_key="" //get it from OpenAI account
client=OpenAI(api_key=api_key)
start = time.time()
response= client.responses.create(
    input="Whats the latest news today in the world of AI"
    tools=[{"type":"web_search_preview"}]
    model="gpt-5-chat"    
)
end = time.time()
elapsed=end-start
print(response.output_text)
print("Response time: %.2f seconds" % elapsed)
