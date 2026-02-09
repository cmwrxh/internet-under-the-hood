import socket
import sys

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{domain} resolves to {ip}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dns_probe.py <domain>")
    else:
        dns_lookup(sys.argv[1])

