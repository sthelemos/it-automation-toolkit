from src.network_check import check_connection

def test_check_connection_returns_dictionary():
    result = check_connection()

    assert isinstance(result, dict)

def test_check_connection_contains_expected_keys():
    result = check_connection()

    expected_keys = {
        "host",
        "ip_address",
        "available",
    }

    assert expected_keys.issubset(result.keys())