import uuid
from enum import StrEnum, auto

from pydantic import BaseModel, EmailStr, Field



class GenderType(StrEnum):
    MALE = auto()
    FEMALE = auto()


class User(BaseModel):
    id: uuid.UUID = uuid.uuid4()
    email: EmailStr
    first_name: str = Field(..., )
    last_name: str = 'Doe'
    gender: GenderType