from enum import Enum
from typing import Annotated

from fastapi import FastAPI, Path, Query, Body, Header

import schemas
import constants

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
        locale: Annotated[constants.LocaleType, Header(..., alias='Accept-Language')],
        name: UserFirstname,
        user: schemas.User = Body(..., alias='User')
) -> dict:
    print(user.json())

    match name:
        case UserFirstname.aibek:
            print('Hello')
        case UserFirstname.a:
            print('Bye')
        case _:
            user.first_name = name

    return {**user.dict(), 'locale': user}
