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

if __name__ == "__main__":
    result = check_http("https://www.google.com") #Change the URL to test other websites

    print(f"URL            : {result['url']}")
    print(f"Status Code    : {result['status_code']}")
    print(f"Response Time  : {result['response_time_ms']} ms")
    print(
        f"Status         : "
        f"{'[OK] Available' if result['available'] else '[ERROR] Unavailable'}"
    )