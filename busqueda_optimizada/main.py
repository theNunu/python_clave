
from my_clave_api import asking_answer
print("-- -- CHAT BASICO -- --")


def chat_bot():
    answer = input("\npregunta cualquier cosa: ")

    asking_answer(answer)


while True:
    chat_bot()
