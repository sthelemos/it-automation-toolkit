from src.system_info import get_system_info

def test_get_system_info_returns_dictionary():
    result = get_system_info()
    assert isinstance(result, dict)

def test_get_system_info_contains_expected_keys():
    result = get_system_info()

    expected_keys = {
        "operating_system",
        "os_version",
        "machine",
        "processor",
    }

    assert expected_keys.issubset(result.keys())