import os

from system_info import get_system_info
from network_check import check_connection

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress Enter to return to the main menu...")

def show_header():
    print("=" * 50)
    print("IT Automation Toolkit")
    print("=" * 50)

def show_menu():
    print("\n")
    print("+--------------------------------+")
    print("|              Menu              |")
    print("+--------------------------------+")
    print("|  1. System Information         |")
    print("|  2. Network check              |")
    print("|  3. Full Health Check          |")
    print("|  4. Exit                       |")
    print("+--------------------------------+")

def show_system_info():
    clear_screen()
    show_header()

    system_info = get_system_info()

    print("\n[System Information]")

    print(f"Operating System: {system_info['operating_system']}")
    print(f"OS Version: {system_info['os_version']}")
    print(f"Machine: {system_info['machine']}")
    print(f"Processor: {system_info['processor']}")

    pause()

def show_network_check():
    clear_screen()
    show_header()

    result = check_connection()

    print("\n[Network Check Result]")

    print(f"Host: {result['host']}")
    print(f"IP Address: {result['ip_address']}")
    print(f"Status: {'Reachable' if result['reachable'] else 'Not Reachable'}")

    pause()

def show_full_health_check():
    clear_screen()
    show_header()

    system_info = get_system_info()
    network_info = check_connection()

    print("\n[Full Health Check Result]")

    print("System")
    print("-" * 50)
    print(f"Operating System: {system_info['operating_system']}")
    print(f"Machine: {system_info['machine']}")
    print(f"Processor: {system_info['processor']}")

    print("\nNetwork")
    print("-" * 50)
    print(f"Host: {network_info['host']}")
    print(f"IP Address: {network_info['ip_address']}")

    if network_info['reachable']:
        print("Status: [OK] Reachable")
    else:
        print("Status: [ERROR] Not Reachable")

    pause()

def main():
    while True:
        clear_screen()
        show_header()
        show_menu()

        option = input("\nSelect an option [1-4]:").strip()

        if option == "1":
            show_system_info()

        elif option == "2":
            show_network_check()

        elif option == "3":
            show_full_health_check()

        elif option == "4":
            print("Exiting...")
            break

        else:
            print("\n[ERROR] Invalid option.")
            print("Please select an option between 1 and 4.")
            pause()

if __name__ == "__main__":
    main()

