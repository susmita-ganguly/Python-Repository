from openai import AzureOpenAI
import base64

client= AzureOpenAI(
    api_versin-"",
    azure_endpoint="",
    api_key="",
)
#we will do a function tool calling within the chat completions API
with open("Invoice.jpg","rb") as image_file:
    document_details=base64.b64encode(image_file.read()).decode("utf-8")

    tools= [{
        "type":"function",
        "function":{
            "name":"return_invoiuce_fields",
            "description":"Return only the extracted invoice fields.",
            "parameters":{
                "type":"object",
                "additionalProperties": False,
                "properties":{
                    "invoice_number":{"type":"string"},
                    "invoice_date":{"type":"string", "description":"YYYY-MM-DD if possible"},
                    "company_name":{"type":"string"},
                    "total_due":{"type":"string"},
                },
                "required":["invoice_number","invoice_date","company_name","total_due"]
            }
        }
    }]
    messages=[
        {"role":"system",
         "content":"Extract strctured information from invoices accurately and concisely"
        },
           { 
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":(
                        "Extract the following and return them via the function call:\n"
                        "-invoice_number (string)\n"
                        "-invoice_date (YYYY-MM-DD if possible)\n"
                        "-company_name (string)\n"
                        "-total_due (number only)\n"
                        "if fields are missing, infer carefully from context."
                    ),
                },
                {
                    "type":"image_url",
                    "image_url": {"url": f"data:image/png;base64,{document_details}"},
                },
            ],
            },
            ]
            resp=client.chat.completions.create(
                model="gpt-5-chat",
                messages=messages,
                tools=tools,
                tool_choice={"type":"function","function":{"name":"return_invoice_fields"}}
            )
    