import pytest
from pytest_mock import MockerFixture
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

def test_load_continue_wait(url: str, token: str,  mocker: MockerFixture):
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json = mocker.MagicMock(side_effect=[{"error": "Continue wait"}, {"error": "Continue wait"}, {"results": []}])

    mock_client = mocker.patch('httpx.Client')
    mock_client.return_value.send.return_value = mock_response
    mock_client.return_value.build_request.return_value = mocker.Mock()

    cube = cube_http.Client({"url": url, "token": token})
    cube.v1.load({})

    assert mock_response.json.call_count == 3

@pytest.mark.asyncio
async def test_async_load_continue_wait(url: str, token: str,  mocker: MockerFixture):
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json = mocker.MagicMock(side_effect=[{"error": "Continue wait"}, {"error": "Continue wait"}, {"results": []}])

    mock_client = mocker.patch('httpx.AsyncClient')
    mock_client.return_value.send = mocker.AsyncMock(return_value=mock_response)
    mock_client.return_value.build_request.return_value = mocker.Mock()

    cube = cube_http.AsyncClient({"url": url, "token": token})
    await cube.v1.load({})

    assert mock_response.json.call_count == 3
