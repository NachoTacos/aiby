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

def mock_exam(client, message):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": f"Eres un tutor dispuesto a ayudar a tu estudiante de nombre {"MariAngela"} de {20}\n años de edad que estudia la carrera de {"Terapia de la comunicacion"} y su forma de\n aprender es {"kinestesico"}. El tutor se encarga de que el aprendizaje sobre temas"
                        "vistos en sus clases.  Es imprescindible, que tu como tutor, en base a las preguntas"
                        f"del alumno y el material escolar proporcionado realices un examen de prueba (mock exam)\n en base al contenido [{"lenguas"}] de la materia de {"linguistica"} generar los siguientes apartados;" 
                        "es importante que los títulos sigan este patrón:"
                        "Titulo"
                        "(Información de contexto e indicaciones del examen"
                        "Pregunta o problema dependiendo de la manera de aprendizaje del alumno"
                        "Opciones junto con la respuesta correcta para comprobar las respuestas del alumno"},
            {"role": "user", "content": message}
        ]
    )
    text = response.choices[0].message.content
    print(text)
    return str(text)

# Function to get the response from my pal chatsito botsito


def code_completion_chat(client, message ):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system",
             "content": f"Eres un tutor dispuesto a ayudar a tu estudiante de nombre {"Mariangela"} de {20} "
                        f"años de edad que estudia la carrera de {"terapias de la comunicacion"} y su forma de"
                        f" aprender es {"kinestesica"}. El tutor se encarga de que el aprendizaje sobre temas"
                        " vistos en sus clases.  Es imprescindible, que tu como tutor, en base a las preguntas"
                        " del alumno y el material escolar proporcionado dividas y resuman el contenido en los"
                        " siguientes puntos con los siguientes títulos, es importante que los títulos sigan"
                        " este patron:"
                        "KEY_TAKEAWAYS"
                        "SUMMARY"
                        "TRANSCRIPTION"},
            {"role": "user", "content": message}
        ]
    )
    text = response.choices[0].message.content
    print(text)
    return str(text)


def split_response(text):
    keywords = ["KEY_TAKEAWAYS", "SUMMARY", "TRANSCRIPTION"]

    pattern = '|'.join([re.escape(keyword) for keyword in keywords])

    split_text = re.split(pattern, text)

    split_text = [section.strip() for section in split_text if section]

    return split_text[0], split_text[1], split_text[2]


def text_to_speech(client, message):
    params = {
        "model": "tts-1",
        "voice": "shimmer",
        "input": message.strip()
    }

    try:
        response = client.audio.speech.create(**params)

        response.stream_to_file("output.mp3")
    except Exception as e:
        print(f"Error: {e}")


message = code_completion_chat(client)
transcription = speech_to_text(client)
text_to_speech(client, message)
var1, var2, var3 = split_response(message)
print(var1, '/n')
print(var2, '/n')
print(var3, '/n')
mock_exam(client, message)
