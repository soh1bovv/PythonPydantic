from pydantic import BaseModel,Field
from typing import Optional
from fastapi import FastAPI

app = FastAPI()
User ={
    'age': 14,
    'name': 'Bob',
    'bio': 'сегодня я ел шаурму'
}

class UserSchema (BaseModel):
    name: str = Field(max_length=10)
    age:int = Field(ge=0, le=150)
    bio:str = Field(min_length=10,max_length=100)
    id: Optional[int] = None

@app.get("/lobby")
def lobby():
    return 'hello'

users = []
current_id = 1

@app.post('/users')
def add_users(user:UserSchema):
    global current_id
    user.id = current_id
    current_id += 1
    users.append(user)
    return{'ok': True, "msg":"юзер на месте", "id": user.id}

@app.get('/users')
def get_users():
    return users

print(UserSchema(**User))