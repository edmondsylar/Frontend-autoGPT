import assemblyai as aai

# Your API token is already set here
aai.settings.api_key = "697ada0609fd42fb92c04208daa519d2"

# Create a transcriber object.
transcriber = aai.Transcriber()

def transcribe(audio_file):
    transcript = transcriber.transcribe(audio_file)
    return transcript.text

# test transcribe("./conv_1.m4a")
# Conversation = transcribe("./ivy_edmond.m4a")
# print(Conversation)