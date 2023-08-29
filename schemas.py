import uuid

from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field, validator

import constants


class Wallet(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    currency: constants.WalletCurrency
    amount: Decimal = Field(max_digits=14, decimal_places=2, gt=0)


class User(BaseModel):
    id: uuid.UUID = Field(..., default_factory=uuid.uuid4)
    email: EmailStr
    first_name: str = Field(..., min_length=1)
    last_name: str = 'Doe'
    gender: constants.GenderType
    wallets: list[Wallet] = Field(min_items=1)

    @validator('first_name')
    def name_must_start_with_a(cls, value: str):
        if not value.lower().startswith('a'):
            raise ValueError('Invalid firstname')

    @validator('wallets', each_item=True)
    def validate_wallets(cls, wallet: Wallet):
        if wallet.amount < 0:
            raise ValueError('value must be greater than 0')

        return wallet.amount


