from unittest.mock import patch, MagicMock
from src.client import get_post, create_post, get_comments

def test_get_post():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 1, "title": "Test"}
    mock_response.raise_for_status.return_value = None
    with patch('src.client.requests.get', return_value=mock_response):
        result = get_post(1)
        assert result["id"] == 1

def test_create_post():
    mock_response = MagicMock()
    mock_response.json.return_value = {"id": 101, "title": "New"}
    mock_response.raise_for_status.return_value = None
    with patch('src.client.requests.post', return_value=mock_response):
        result = create_post("New", "Body", 1)
        assert result["id"] == 101

def test_get_comments():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "body": "Comment"}]
    mock_response.raise_for_status.return_value = None
    with patch('src.client.requests.get', return_value=mock_response):
        result = get_comments(1)
        assert len(result) == 1
