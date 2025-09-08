import getpass
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")


# os.environ["GOOGLE_API_KEY"] = "AIzaSyCVe_YsKglUkMP-0fsc24wuP75av2-iCsI"
if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("GOOGLE_API_KEY")


def responder_pregunta(pregunta: str) -> str:
  
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

    respuesta = model.invoke(pregunta)
    print(respuesta.content)
    


