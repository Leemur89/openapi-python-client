from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import File, Response


def _get_kwargs(
    *,
    binary_body: File,
) -> Dict[str, Any]:
    headers = {}
    headers["Content-Type"] = binary_body.mime_type if binary_body.mime_type else "application/octet-stream"

    return {
        "method": "post",
        "url": "/tests/octet_stream",
        "content": binary_body.payload,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, str]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    binary_body: File,
) -> Response[Union[HTTPValidationError, str]]:
    """Binary (octet stream) request body

    Args:
        binary_body (File): A file to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        binary_body=binary_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    binary_body: File,
) -> Optional[Union[HTTPValidationError, str]]:
    """Binary (octet stream) request body

    Args:
        binary_body (File): A file to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return sync_detailed(
        client=client,
        binary_body=binary_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    binary_body: File,
) -> Response[Union[HTTPValidationError, str]]:
    """Binary (octet stream) request body

    Args:
        binary_body (File): A file to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, str]]
    """

    kwargs = _get_kwargs(
        binary_body=binary_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    binary_body: File,
) -> Optional[Union[HTTPValidationError, str]]:
    """Binary (octet stream) request body

    Args:
        binary_body (File): A file to upload

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, str]
    """

    return (
        await asyncio_detailed(
            client=client,
            binary_body=binary_body,
        )
    ).parsed
