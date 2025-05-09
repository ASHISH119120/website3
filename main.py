
import port_scanner
import brute_forcer

def main():
    print("=== 🛠️ Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        target = input("Enter target IP address or domain: ")
        ports = [21, 22, 23, 80, 443, 8080]
        port_scanner.scan_ports(target, ports)

    elif choice == '2':
        username = input("Enter username: ")
        correct_password = "admin123"  # simulate correct password
        password_list = ["123", "admin", "password", "admin123"]
        brute_forcer.brute_force_login(username, password_list, correct_password)

    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
