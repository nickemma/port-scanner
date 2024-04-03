import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

# Set the IP address and port number of the server to connect to in a function
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(termcolor.colored("[+] Port Opened ", "green" + str(port)))
        socket.close()
    except:
        print(termcolor.colored("[-] Port Closed ", "red" + str(port)))

        
targets = input("[*] Enter Targets To Scan (split them by ,): ")
ports = input("[*] Enter How Many Ports You Want To Scan: ")

if "," in targets:
    print(termcolor.colored("[*] Scanning Multiple Targets", "blue"))
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(" "), ports)
else:
    scan(targets, ports)