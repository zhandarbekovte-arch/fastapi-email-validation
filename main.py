from fastapi import FastAPI
from pydantic import BaseModel, EmailStr


app = FastAPI()


class User(BaseModel):
    name: str
    email: EmailStr


@app.post("/register")
async def register(user: User):
    """
    Қолданушыны тіркеу эндпойнты.
    Email Pydantic арқылы автоматты тексеріледі.
    """
    # Егер email жарамсыз болса, Pydantic автоматты қате қайтарады
    return {
        "message": "Қолданушы сәтті тіркелді",
        "name": user.name,
        "email": user.email,
    }
