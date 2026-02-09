import subprocess
import sys

def traceroute(host):
    try:
        subprocess.run(["tracert", host])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python trace_route.py <host>")
    else:
        traceroute(sys.argv[1])

