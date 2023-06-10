import openai

class Gpt():
    def __init__(self, api_key) -> None:
        openai.api_key = api_key


    def call_gpt(self, content):
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
        return chat_completion.choices[0].message.content 