from src.http_check import check_http

def test_check_http_return_dictionary():
    result = check_http("https://www.google.com") #Change the URL to test other websites

    assert isinstance(result, dict)

def test_check_http_contains_expected_keys():
    result = check_http("https://www.google.com") #Change the URL to test other websites

    expected_keys = {
        "url",
        "status_code",
        "response_time_ms",
        "available",
    }

    assert expected_keys.issubset(result.keys())

def test_check_http_successful_response():
    result = check_http("https://www.google.com") #Change the URL to test other websites

    assert result["status_code"] == 200
    assert result["available"] is True
    assert result["response_time_ms"] >= 0
    