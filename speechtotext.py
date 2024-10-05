import re
from openai import OpenAI

client = OpenAI(
api_key="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"
)



# Function that converts speech to text with the api
def speech_to_text(client):
    audio_file = open("audio.m4a", "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription

print(speech_to_text(client))