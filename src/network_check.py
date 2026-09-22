import socket
from unittest import result

def check_connection(host="google.com"):
    try:
        ip_address = socket.gethostbyname(host)

        return {
            "host": host,
            "ip_address": ip_address,
            "reachable": True,
        }
    except socket.gaierror:
        return {
            "host": host,
            "ip_address": None,
            "reachable": False,
        }

if __name__ == "__main__":
    check_connection()

    print (f"Host: {result['host']}")
    print (f"IP Address: {result['ip_address']}")
    print (f"Status: {'Reachable' if result['reachable'] else 'Not Reachable'}")