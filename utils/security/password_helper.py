# -*- coding: utf-8 -*-
from typing import Optional, Tuple

from argon2 import PasswordHasher

PASSWORD_VALIDATIONS = [
    {
        "message": "Password must be has minimum 10 characters.",
        "regex": r"^(?=.{8,})",
    },
    {
        "message": "At least one lowercase and uppercase characters.",
        "regex": r"(?=.*[a-z])(?=.*[A-Z])",
    },
    {
        "message": "At least one number.",
        "regex": r"(?=.*[0-9])",
    },
]


class PasswordHelper:
    def __init__(
        self,
        context: Optional[PasswordHasher] = None,
    ) -> None:
        if context is None:
            self.context = PasswordHasher()
        else:
            self.context = context

    def verify_and_update(
        self,
        plain_password: str,
        hashed_password: str,
    ) -> Tuple[bool, str]:
        try:
            self.context.verify(hashed_password, plain_password)
            return True, hashed_password
        except Exception as e:
            return False, str(e)

    def hash(
        self,
        password: str,
    ) -> str:
        return self.context.hash(password)


password_helper = PasswordHelper()