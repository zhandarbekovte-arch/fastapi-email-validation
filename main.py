from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr

@app.post("/register")
def register_user(user: User):
    return {
        "message": "Қолданушы сәтті тіркелді",
        "name": user.name,
        "email": user.email
    }
