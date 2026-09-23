from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

from src.http_check import check_http

def test_check_http_successful_response():
    mock_response = MagicMock()
    mock_response.status = 200

    with patch("src.http_check.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value.__enter__.return_value = mock_response

        result = check_http("https://www.example.com") 

    assert result["status_code"] == 200
    assert result["available"] is True
    assert result["response_time_ms"] >= 0

    mock_urlopen.assert_called_once_with(
    "https://www.example.com",
    timeout=10,
    )

def test_check_http_http_error():
    with patch("src.http_check.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = HTTPError(
            url="https://www.example.com",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None,
        )

        result = check_http("https://www.example.com") 

    assert result["status_code"] == 404
    assert result["available"] is False

def test_check_http_return_dictionary():
    mock_response = MagicMock()
    mock_response.status = 200

    with patch("src.http_check.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.return_value.__enter__.return_value = mock_response


        result = check_http("https://www.example.com") 

    assert result["status_code"] == 200
    assert result["available"] is True
    assert result["response_time_ms"] >= 0

def test_check_http_connection_error():
    with patch("src.http_check.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = URLError("Connection failed")

        result = check_http("https://www.example.com") 
    assert result["status_code"] is None
    assert result["available"] is False

def test_check_http_timeout():
    with patch("src.http_check.urllib.request.urlopen") as mock_urlopen:
        mock_urlopen.side_effect = TimeoutError()

        result = check_http("https://www.example.com") 

    assert result["status_code"] is None
    assert result["available"] is False