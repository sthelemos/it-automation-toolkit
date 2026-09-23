import time
import urllib.request
import urllib.error

def check_http(url):
    start_time = time.perf_counter()

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            response_time = (time.perf_counter() - start_time) * 1000

            return {
                "url": url,
                "status_code": response.status,
                "response_time_ms": round(response_time, 2),
                "available": True,
            }

    except urllib.error.HTTPError as error:
            response_time = (time.perf_counter() - start_time) * 1000

            return {
                "url": url,
                "status_code": error.code,
                "response_time_ms": round(response_time, 2),
                "available": False,
            }

    except urllib.error.URLError:
            response_time = (time.perf_counter() - start_time) * 1000

            return {
            "url": url,
            "status_code": None,
            "response_time_ms": round(response_time, 2),
            "available": False,
        }

    except TimeoutError:
            response_time = (time.perf_counter() - start_time) * 1000

            return {
                "url": url,
                "status_code": None,
                "response_time_ms": round(response_time, 2),
                "available": False,
            }
