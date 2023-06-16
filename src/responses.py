from chatgpt import Gpt
import os

def handle_response(message):
    gpt = Gpt(os.getenv("openai_api_key"))
    print('handle response')

    print(message)
    return(gpt.call_gpt(message))
