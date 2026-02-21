import csv
import platform
import subprocess
from datetime import datetime

TARGETS = ["google.com", "cloudflare.com", "netflix.com"]
COUNT = 5

def ping_avg_ms(host: str, count: int = COUNT) -> float:
    system = platform.system().lower()

    if "windows" in system:
        cmd = ["ping", "-n", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), host]

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=30)
    except Exception:
        return 0.0

    lines = out.splitlines()

    # Linux/macOS parsing
    for line in lines:
        if "min/avg" in line or "round-trip" in line:
            parts = line.split("=")[-1].strip().split()[0].split("/")
            if len(parts) >= 2:
                try:
                    return float(parts[1])
                except ValueError:
                    pass

    # Windows parsing
    for line in lines:
        if "Average" in line:
            try:
                val = line.split("Average")[-1].replace("=", "").replace("ms", "").strip()
                return float(val)
            except ValueError:
                pass

    return 0.0

def main():
    ts = datetime.utcnow().isoformat() + "Z"
    rows = []
    for host in TARGETS:
        avg = ping_avg_ms(host)
        rows.append({"timestamp_utc": ts, "host": host, "avg_rtt_ms": avg})

    # Save to CSV
    with open("latency_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp_utc", "host", "avg_rtt_ms"])
        writer.writeheader()
        writer.writerows(rows)

    print("Successfully wrote latency_results.csv")
    for r in rows:
        print(r)

if __name__ == "__main__":
    main()
