import socket

def scan(target, ports):
    print("\n" + "Starting Scan For Target " + target)
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(3)  # Increased timeout to 3 seconds
        sock.connect((ipaddress, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except Exception as e:
        print("[!] An error occurred:", e)

targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))

if "," in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)
