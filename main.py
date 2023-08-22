import uuid
from enum import Enum

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserFirstname(str, Enum):
    aibek = 'Aibek'
    a = 'A'
    i = 'I'


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    email: EmailStr
    first_name: str = 'John'
    last_name: str = 'Doe'


@app.get('/calc/{num1}-{num2}')
def hello(
    num1: int = Path(...),
    num2: int = Path(...),
    num3: int = Query(None, deprecated=True)
):
    return {'Message': num1 + num2 }


@app.post('/users/{name}', response_model=User, tags=['Users'], deprecated=True)
async def bye(name: UserFirstname, user: User = Body(...)):
    match name:
        case UserFirstname.aibek:
            print('Hello')
        case UserFirstname.a:
            print('Bye')
        case _:
            print('------------')
    user.first_name = name
    return user