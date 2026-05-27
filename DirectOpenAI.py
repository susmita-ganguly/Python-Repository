import openai from OpenAI
api_key="" //get it from OpenAI account
client=OpenAI(api_key=api_key)

response= client.responses.create(
    input=[
        {
            "role":"user",
            "content":"How can I write a simple python code to iteract with OpenAI model"
    
        }],
        
        max_output_token=10000,
        model="gpt-5-chat"    
)
print(response.output_text)

#this should work fine, now we will change the input a bit, 
#we will ask gpt-5 to use its inbuilt image generator tool, referto DirectOpenAI_Imagegen file