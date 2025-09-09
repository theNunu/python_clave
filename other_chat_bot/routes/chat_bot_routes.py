from typing import Union

from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from api_gemini import responder_pregunta

app = FastAPI(title="un bot nuevo")
router = APIRouter()
class Person(BaseModel):
    name: str
    last_name: str
    age: int

class ChatBot(BaseModel):
    pregunta: str
    respuesta: str
    
@app.get("/")
def read_root():
    return {"Hello": "World"}

@router.post("/guardar_person")
def read_item(persona: Person):
    return {"message": "persona creada!!!",
            "nombre": persona.name,
            "apellido": persona.last_name,
            "edad": persona.age
            }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/hacer_pregunta")
def ask_answer(chatbot: ChatBot):
    respuesta_bot = responder_pregunta(chatbot.pregunta)
    
    
    return {
        "message": "chatbot respondiendo",
        "pregunta": chatbot.pregunta,
        "respuesta": respuesta_bot

    }
    