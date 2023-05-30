#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
from time import sleep
from rich.console import Console

# debung console
console = Console()

# engine is the deployment name in my azure resource.

class AzureAuth_v1:
    def __init__(self, api_key, api_base, api_version, deployment_name):
        self.api_type = "azure" 
        self.api_key = api_key
        self.api_base = api_base
        self.api_version = api_version
        self.deployment_name = deployment_name

        # declare chat_history variable to capture chat conversations and enable continuing conversations.
        self.chat_history = [
            {"role": "system", "content": "You are a general Purpose AI assistant, you help people accomplish their goals."},
        ]

        # authenticate with openai
        self.Authenticate()

    def _build_chat_history(self, assistant_response):
        # build a histtoy block.
        assistant = {
            "role": "assistant",
            "content": assistant_response
            }
        self.chat_history.append(assistant)

    def Authenticate(self):
        openai.api_type = self.api_type
        openai.api_base = self.api_base
        openai.api_version = self.api_version
        openai.api_key = self.api_key
    
    def _testAuth(self):
        test_msg = """
          This Mesage is comming from a user to test if there have been a connection established with the cloud service.
          Respond to the user with a fun message showing there have Been a connection. Attach a fun internet Joke.
        """

        res = openai.Completion.create(
            engine=self.deployment_name,
            prompt=test_msg,
            max_tokens = 800,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        return (res['choices'][0]['text'])
    
    def chat(self, prompt):
        self.chat_history.append(
            {"role": "user", "content": prompt}
        )
        res = openai.ChatCompletion.create(
            engine=self.deployment_name,
            messages = self.chat_history,
            max_tokens = 800,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )

        _res = res['choices']
        _temp_msg = _res[0]
        _msg = _temp_msg['message']['content']
        return (_msg)


        


      