from typing import Any

from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


class RFC9457Schema:
    type: str
    title: str
    detail: str
    instance: str


def better_exception_handler(
    exc: Exception | APIException, context: dict[str, Any]
) -> Response | None:
    response: Response | None = exception_handler(exc, context)

    if response is not None:
        return Response()

    return None
