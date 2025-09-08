from api_gemini import responder_pregunta


def chat_bot_google():
    anwser = input("\npregunta cualquier cosa:")

    responder_pregunta(anwser)


while True:
    chat_bot_google()