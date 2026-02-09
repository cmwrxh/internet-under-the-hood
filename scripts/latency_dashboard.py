import subprocess
import pandas as pd

targets = ["google.com", "cloudflare.com", "netflix.com"]

results = []

for host in targets:
    output = subprocess.getoutput(f"ping -c 5 {host}")
    for line in output.split("\n"):
        if "avg" in line:
            avg = line.split("/")[4]
            results.append({"host": host, "avg_rtt_ms": avg})

df = pd.DataFrame(results)
print(df)
df.to_csv("latency_results.csv", index=False)


---

## 4) Replace / add scripts (robust + CI-safe)

### `scripts/latency_dashboard.py` (CI-safe, outputs CSV)
```python
import csv
import platform
import subprocess
from datetime import datetime

TARGETS = ["google.com", "cloudflare.com", "netflix.com"]
COUNT = 5

def ping_avg_ms(host: str, count: int = COUNT) -> float | None:
    system = platform.system().lower()

    if "windows" in system:
        cmd = ["ping", "-n", str(count), host]
    else:
        cmd = ["ping", "-c", str(count), host]

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True, timeout=30)
    except Exception:
        return None

    # Parse averages for Windows/Linux/macOS variants
    lines = out.splitlines()

    # Linux/macOS often have: rtt min/avg/max/mdev = 10.1/12.3/...
    for line in lines:
        if "min/avg" in line or "round-trip" in line:
            # grab numbers like 10.1/12.3/...
            parts = line.split("=")[-1].strip().split()[0].split("/")
            if len(parts) >= 2:
                try:
                    return float(parts[1])
                except ValueError:
                    pass

    # Windows has: Average = 23ms
    for line in lines:
        if "Average" in line:
            # e.g. "Average = 23ms"
            try:
                val = line.split("Average")[-1].replace("=", "").replace("ms", "").strip()
                return float(val)
            except ValueError:
                pass

    return None

def main() -> None:
    ts = datetime.utcnow().isoformat() + "Z"
    rows = []
    for host in TARGETS:
        avg = ping_avg_ms(host)
        rows.append({"timestamp_utc": ts, "host": host, "avg_rtt_ms": avg})

    with open("latency_results.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["timestamp_utc", "host", "avg_rtt_ms"])
        writer.writeheader()
        writer.writerows(rows)

    print("Wrote latency_results.csv")
    for r in rows:
        print(r)

if __name__ == "__main__":
    main()
