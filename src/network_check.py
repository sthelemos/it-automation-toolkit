import socket

def check_connection(host="google.com"):
    try:
        ip_address = socket.gethostbyname(host)
        print(f"Host: {host}")
        print(f"IP Address: {ip_address}")
        print("Status: Reachable")

    except socket.gaierror:
        print(f"Host: {host}")
        print("Status: Unreachable")

if __name__ == "__main__":
    check_connection()