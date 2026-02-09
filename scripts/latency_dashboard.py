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
