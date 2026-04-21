from unittest.mock import patch, MagicMock, AsyncMock
import pytest
from src.client import get_post, create_post, get_comments

@pytest.mark.asyncio
async def test_get_post():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Test"}
    mock_response.raise_for_status.return_value = None
    with patch('src.client.httpx.AsyncClient', create=True) as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_post(1)
        assert result["id"] == 1

@pytest.mark.asyncio
async def test_create_post():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 101, "title": "New"}
    mock_response.raise_for_status.return_value = None
    with patch('src.client.httpx.AsyncClient', create=True) as MockClient:
        mock_client = AsyncMock()
        mock_client.post.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await create_post("New", "Body", 1)
        assert result["id"] == 101

@pytest.mark.asyncio
async def test_get_comments():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "body": "Comment"}]
    mock_response.raise_for_status.return_value = None
    with patch('src.client.httpx.AsyncClient', create=True) as MockClient:
        mock_client = AsyncMock()
        mock_client.get.return_value = mock_response
        mock_client.__aenter__.return_value = mock_client
        mock_client.__aexit__.return_value = None
        MockClient.return_value = mock_client
        result = await get_comments(1)
        assert len(result) == 1
