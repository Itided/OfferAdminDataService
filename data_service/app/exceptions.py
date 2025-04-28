import typing

from litestar import status_codes, Response, MediaType


class JsonErrorResponse:
    default_detail = "Something went wrong"
    default_status_code = status_codes.HTTP_500_INTERNAL_SERVER_ERROR

    @classmethod
    def to_response(cls, detail: str = None, status_code: int = None):
        return Response(
            media_type=MediaType.JSON,
            content={"message": detail or cls.default_detail},
            status_code=status_code or cls.default_status_code,
        )


class NotFound(Exception, JsonErrorResponse):
    default_detail = "Not found"
    default_status_code = status_codes.HTTP_404_NOT_FOUND


# Handlers
def handle_not_found(request, exc) -> Response[dict[str, typing.Any]]:
    return exc.to_response()
