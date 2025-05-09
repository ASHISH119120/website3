# port_scanner.py
import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning ports on {target}...\n")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"✅ Port {port} is open")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
