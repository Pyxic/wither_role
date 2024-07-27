# -*- coding: utf-8 -*-
from pydantic import Field
from utils.schemas.base import EmailSchema


class LoginSchema(EmailSchema):
    """
    Class to check the user in the /login endpoint.
    """

    password: str = Field(description="The user's password.", min_length=8)


class UserPayload(EmailSchema):
    id: int
    username: str

    async def get_instance(self, user_repository):
        return await user_repository.get_single(id=self.id)




class UserCreateSchema(EmailSchema):
    password: str = Field(description="The user's password.", min_length=8)
    username: str = Field(min_length=8)
