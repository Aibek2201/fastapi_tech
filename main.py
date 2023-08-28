from enum import Enum

from fastapi import FastAPI, Path, Query, Body

import schemas

app = FastAPI()


class UserFirstname(str, Enum):
    aibek = 'Aibek'
    a = 'A'
    i = 'I'


@app.get('/calc/{num1}-{num2}')
def hello(
    num1: int = Path(...),
    num2: int = Path(...),
    num3: int = Query(None)
):
    return {'Message': num1 + num2 + num3}


@app.post('/users/{name}', tags=['users'])
async def bye(
        name: UserFirstname,
        user: schemas.User = Body(..., alias='User')
) -> schemas.User:
    print(user.json())

    match name:
        case UserFirstname.aibek:
            print('Hello')
        case UserFirstname.a:
            print('Bye')
        case _:
            print('------------')
    user.first_name = name
    return user
