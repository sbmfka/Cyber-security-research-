import socket

# This is a basic port scanner for CEH v13 Phase 2 (Scanning)
def scan_target(ip):
    # Common ports: 21(FTP), 22(SSH), 80(HTTP), 443(HTTPS)
    target_ports = [21, 22, 80, 443]
    
    print(f"--- Starting Scan on: {ip} ---")
    
    for port in target_ports:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Wait 1 second for a response
        
        # Try to connect to the port
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")
            
        s.close()
    print("--- Scan Complete ---")

if __name__ == "__main__":
    # 127.0.0.1 is your "Home" address (loopback)
    # Never scan IPs you do not own!
    target_ip = "127.0.0.1" 
    scan_target(target_ip)
