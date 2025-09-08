import getpass
import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

# Cargar .env
load_dotenv()

# Obtener API key
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    api_key = getpass.getpass("Tavily API key:\n")
    os.environ["TAVILY_API_KEY"] = api_key

# Inicializar herramienta
tool = TavilySearch(
    max_results=20,
    topic="general",
)

def responder_pregunta(pregunta):
    print("cargando respuesta .... ")

    model_generated_tool_call = {
        "args": {"query": pregunta},
        "id": "1",
        "name": "tavily",
        "type": "tool_call",
    }
    tool_msg = tool.invoke(model_generated_tool_call)
    print(tool_msg.content[:400])


# Ejemplo
# responder_pregunta("¿Cómo ocurrió la caída de Constantinopla?")
