import os

from system_info import get_system_info
from network_check import check_connection
from http_check import check_http


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to return to the main menu...")


def show_header():
    print("=" * 50)
    print("             IT AUTOMATION TOOLKIT")
    print("=" * 50)


def show_menu():
    print("\n")
    print("+----------------------------------------------+")
    print("|                   MENU                       |")
    print("+----------------------------------------------+")
    print("|  1. System Information                       |")
    print("|  2. Network Check                            |")
    print("|  3. HTTP/API Health Check                    |")
    print("|  4. Full Health Check                        |")
    print("|  5. Exit                                     |")
    print("+----------------------------------------------+")


def show_system_info():
    clear_screen()
    show_header()

    system_info = get_system_info()

    print("\n[ SYSTEM INFORMATION ]\n")

    print(f"Operating System : {system_info['operating_system']}")
    print(f"OS Version       : {system_info['os_version']}")
    print(f"Machine          : {system_info['machine']}")
    print(f"Processor        : {system_info['processor']}")

    pause()


def show_network_check():
    clear_screen()
    show_header()

    print("\n[ NETWORK CHECK ]\n")

    host = input("Enter the hostname or IP address: ").strip()

    if not host:
        print("\n[ERROR] Hostname or IP address cannot be empty.")
        pause()
        return

    result = check_connection(host)

    print("\n[ RESULT ]")
    print("-" * 50)
    print(f"Host             : {result['host']}")
    print(f"IP Address       : {result['ip_address']}")

    if result["available"]:
        print("Status           : [OK] Available")
    else:
        print("Status           : [ERROR] Unavailable")

    pause()


def show_http_check():
    clear_screen()
    show_header()

    print("\n[ HTTP/API HEALTH CHECK ]\n")

    url = input("Enter the URL to check: ").strip()

    if not url:
        print("\n[ERROR] URL cannot be empty.")
        pause()
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    result = check_http(url)

    print("\n[ RESULT ]")
    print("-" * 50)
    print(f"URL              : {result['url']}")
    print(f"Status Code      : {result['status_code']}")
    print(f"Response Time    : {result['response_time_ms']} ms")

    if result["available"]:
        print("Status            : [OK] Available")
    else:
        print("Status            : [ERROR] Unavailable")

    pause()


def show_full_health_check():
    clear_screen()
    show_header()

    print("\n[ FULL HEALTH CHECK ]\n")

    host = input("Enter hostname or IP address: ").strip()

    if not host:
        print("\n[ERROR] Hostname or IP address cannot be empty.")
        pause()
        return

    url = input("Enter URL for HTTP check: ").strip()

    if not url:
        print("\n[ERROR] URL cannot be empty.")
        pause()
        return

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    system_info = get_system_info()
    network_info = check_connection(host)
    http_info = check_http(url)

    print("\nSYSTEM")
    print("-" * 50)
    print(f"Operating System : {system_info['operating_system']}")
    print(f"OS Version       : {system_info['os_version']}")
    print(f"Machine          : {system_info['machine']}")
    print(f"Processor        : {system_info['processor']}")

    print("\nNETWORK")
    print("-" * 50)
    print(f"Host             : {network_info['host']}")
    print(f"IP Address       : {network_info['ip_address']}")

    if network_info["available"]:
        print("Status           : [OK] Available")
    else:
        print("Status           : [ERROR] Unavailable")

    print("\nHTTP/API")
    print("-" * 50)
    print(f"URL              : {http_info['url']}")
    print(f"Status Code      : {http_info['status_code']}")
    print(f"Response Time    : {http_info['response_time_ms']} ms")

    if http_info["available"]:
        print("Status            : [OK] Available")
    else:
        print("Status            : [ERROR] Unavailable")

    pause()


def main():
    while True:
        clear_screen()
        show_header()
        show_menu()

        option = input("\nSelect an option [1-5]: ").strip()

        if option == "1":
            show_system_info()

        elif option == "2":
            show_network_check()

        elif option == "3":
            show_http_check()

        elif option == "4":
            show_full_health_check()

        elif option == "5":
            clear_screen()
            show_header()
            print("\nThank you for using IT Automation Toolkit.")
            print("Goodbye!\n")
            break

        else:
            print("\n[ERROR] Invalid option.")
            print("Please select an option between 1 and 5.")
            pause()


if __name__ == "__main__":
    main()