# -*- coding: utf-8 -*-
import abc
import typing
from abc import abstractproperty
from typing import Any, Union

from fastapi import HTTPException  # noqa
from fastapi_babel.core import lazy_gettext


class ClassABC(type):

    # flake8: noqa: C901
    def __init__(cls, name, bases, attrs):
        abstracts = set()

        for base in bases:
            abstracts.update(getattr(base, "__abstractclassmethods__", set()))

        for abstract in abstracts:
            annotation_type = bases[0].__annotations__.get(abstract)
            if annotation_type:
                if annotation_type == Any:
                    continue
                if not typing.get_origin(annotation_type) == typing.Union:
                    # For non-Union types, use isinstance()
                    if not isinstance(getattr(cls, abstract), annotation_type):
                        raise TypeError("Wrong type of {}".format(abstract))
                else:
                    # For Union types, check each type in the Union
                    is_correct_type = False
                    for t in typing.get_args(annotation_type):
                        if isinstance(getattr(cls, abstract), t):
                            is_correct_type = True
                    if not is_correct_type:
                        raise TypeError("Wrong type of {}".format(abstract))

                if getattr(getattr(cls, abstract), "__isabstractmethod__", False):
                    raise TypeError("Your class doesn't define {}".format(abstract))

        for attr in attrs:
            if getattr(attrs[attr], "__isabstractmethod__", False):
                abstracts.add(attr)

        cls.__abstractclassmethods__ = abstracts

        super().__init__(name, bases, attrs)


class BaseHTTPException(HTTPException, metaclass=ClassABC):
    status_code: int = 400

    def __init__(self, headers: typing.Optional[typing.Dict[str, Any]] = None) -> None:
        super().__init__(status_code=self.status_code, headers=headers)

    @abc.abstractmethod
    def example(self) -> dict:
        pass


class DefaultHTTPException(BaseHTTPException):
    error: str = abstractproperty()
    message: Any = abstractproperty()

    def __init__(
        self,
        message: Union[str, "__LazyText"] = None,
        headers: typing.Optional[typing.Dict[str, Any]] = None,
    ):  # noqa
        print(type(self.message))
        self.message = str(message) if message else str(self.message)
        super(DefaultHTTPException, self).__init__(headers=headers)

    def example(self) -> dict:
        example = {
            "summary": self.error,
            "value": [
                {
                    "statusCode": self.status_code,
                    "error": self.error,
                    "message": self.message.message if isinstance(self.message, lazy_gettext) else self.message,
                },
            ],
        }
        return example
