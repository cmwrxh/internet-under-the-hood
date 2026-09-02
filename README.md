# African Network Latency Optimization

Production-ready configurations and benchmarks for reducing API latency across African mobile networks.

**Problem:** APIs serving African users often resolve DNS through Europe, handshake TLS across the Atlantic, and route packets through suboptimal BGP paths—adding 200–400ms before any application logic runs.

**Solution:** This repository documents how to cut that overhead by 60–75% using edge routing, TLS tuning, and local peering optimization.

---

## Benchmark: Nairobi to API Endpoint

Test conditions: Safaricom 4G, Karen, Nairobi. Target: US-East-1 origin.

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| DNS Resolution | 120ms | 15ms | -87% |
| TLS Handshake (1.2) | 180ms | 45ms | -75% |
| TTFB (Time to First Byte) | 380ms | 95ms | -75% |
| p99 Latency | 420ms | 110ms | -74% |

**Test tool:** `curl -w "@curl-format.txt" -o /dev/null -s [endpoint]`

---

## What Changed

### 1. DNS: Geo-Steering + Local Resolver

**Before:** Queries hit `8.8.8.8`, routed to Google DNS in London, then to authoritative nameservers in Virginia.

**After:** Cloudflare DNS with geo-steering. Authoritative NS placed at Cloudflare edge nodes in Nairobi and Mombasa.

```bash
# Before traceroute
$ dig +trace api.example.com @8.8.8.8
;; Received 512 bytes from 216.239.32.10#53(216.239.32.10) in 118 ms
;; Received 512 bytes from 205.251.197.141#53(205.251.197.141) in 312 ms

# After traceroute
$ dig +trace api.example.com @1.1.1.1
;; Received 512 bytes from 172.64.32.1#53(172.64.32.1) in 12 ms
;; Received 512 bytes from 108.162.193.141#53(108.162.193.141) in 8 ms
