# -*- coding: utf-8 -*-
from pydantic import BaseModel, EmailStr, Field, field_validator


class BaseSchema(BaseModel):
    class Config:
        populate_by_name = True
        from_attributes = True


class EmailSchema(BaseSchema):
    email: EmailStr = Field(description="The user's email.")

    @field_validator("email")
    def email_to_lower(cls, v):
        """
        Convert email to lower case.
        """
        return v.lower()
