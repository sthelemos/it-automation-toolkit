import socket

def check_connection(host):
    try:
        ip_address = socket.gethostbyname(host)

        return {
            "host": host,
            "ip_address": ip_address,
            "available": True,
        }

    except socket.gaierror:
        return {
            "host": host,
            "ip_address": None,
            "available": False,
        }