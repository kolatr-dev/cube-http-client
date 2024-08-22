import pytest

import cube_http
from cube_http.types.v1.load import V1LoadRequestQueryDict

from .fixtures import TEST_QUERIES


@pytest.mark.parametrize("query", TEST_QUERIES)
def test_load(url: str, token: str, query: V1LoadRequestQueryDict):
    cube = cube_http.Client({"url": url, "token": token})
    result = cube.v1.load(query)
    assert result is not None


@pytest.mark.parametrize("query", TEST_QUERIES)
@pytest.mark.asyncio
async def test_async_load(url: str, token: str, query: V1LoadRequestQueryDict):
    cube = cube_http.AsyncClient({"url": url, "token": token})
    result = await cube.v1.load(query)
    assert result is not None
